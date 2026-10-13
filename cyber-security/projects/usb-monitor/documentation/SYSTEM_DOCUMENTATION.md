# System Architecture & Technical Documentation

## 1. Project Overview & Objective

The **Consent-Based USB Activity Monitoring System** is an educational defensive cybersecurity tool. In modern enterprise and laboratory environments, USB peripheral devices are frequent attack vectors for physical data exfiltration and malicious payload injection (e.g., BadUSB). 

This project demonstrates how defensive host-monitoring applications operate transparently while upholding strict privacy and ethical boundaries:
- **Explicit Informed Consent:** Monitoring cannot initialize until the user explicitly agrees via a consent prompt.
- **Strict Privacy Scope:** The application does not log keystrokes, capture credentials, read browsing history, touch webcams, or transmit data over the network.
- **Cryptographic Audit Trail:** Activity logs are signed with SHA-256 hashes to guarantee data integrity and detect tampering.

---

## 2. Linux Kernel & File System Capture Mechanism

### How Linux Detects USB Events
Linux handles USB hardware discovery and lifecycle events through the kernel and the user-space device manager **udev**:

```
[ Physical USB Plug/Unplug ]
              │
              ▼
   Linux Kernel (Driver Core)
              │
     Netlink Socket Broadcast
              │
              ▼
         udev Daemon
              │
      pyudev (Netlink Poll)
              │
              ▼
    usb_monitor.py (_monitor_linux)
              │
              ├─ Filters: device_type == 'usb_device'
              ├─ Reads Hardware IDs from sysfs
              └─ Correlates with /proc/mounts & SCSI Block Subsystem
```

1. **Kernel Netlink Sockets:** When a USB device is plugged in, the kernel USB core detects electrical line state changes and generates a `uevent` broadcast over an asynchronous kernel Netlink socket.
2. **Device Discovery via `sysfs` (`/sys`):** The kernel populates metadata in `/sys/bus/usb/devices/` including Vendor ID (`ID_VENDOR_ID`), Product ID (`ID_MODEL_ID`), Serial Number (`ID_SERIAL_SHORT`), and USB speed.
3. **Filtering Physical Devices vs. Interfaces:** 
   - A single physical USB device exposes one parent device (`DEVTYPE=usb_device`) and one or more functional endpoints (`DEVTYPE=usb_interface`).
   - The monitor filters strictly for `device.device_type == "usb_device"` to prevent duplicate event triggers.
4. **Storage Subsystem Correlation:**
   - When a USB mass storage device (`ID_USB_INTERFACES` contains `:08`) is detected, the kernel registers a SCSI block device (`/dev/sdX` or `/dev/nvmeX`).
   - The application inspects the `block` subsystem, matching block device tree paths to the parent USB controller.
5. **Filesystem & Mount Point Resolution:**
   - Inspects volume labels (`ID_FS_LABEL`), filesystem type (`ID_FS_TYPE`), and UUIDs.
   - Reads `/proc/mounts` to determine if and where the system mounted the volume.

---

## 3. Platform Status: Windows Pending

* **Linux:** **Fully Implemented & Operational** via `pyudev`, `/sys`, and `/proc/mounts`.
* **Windows:** **Pending Implementation.**
  - Windows requires Windows Management Instrumentation (WMI) event queries (`__InstanceCreationEvent` on `Win32_USBHub` / `Win32_DiskDrive`) or Win32 device notification window procedures via `pywin32`.
  - Windows-specific detection is currently stubbed out in `monitor/usb_monitor.py` (`_start_monitoring_windows`) for future laboratory expansion.

---

## 4. Cryptographic Integrity (Stage 8)

To prove that log entries have not been tampered with or modified post-capture:
1. Upon monitoring shutdown, the entire log (`reports/activity_log.json`) is read in 4096-byte binary chunks and hashed using **SHA-256**.
2. The hash digest is saved to `reports/activity_log.json.sha256`.
3. Running with `--demo-tamper` intentionally injects a forged byte into the log to demonstrate how the integrity verification immediately catches unauthorized modifications.

---

## 5. Generated Audit Formats

All outputs reside strictly in `reports/`:
- **JSON (`activity_log.json`):** Machine-readable structured log.
- **Digest (`activity_log.json.sha256`):** Cryptographic verification record.
- **Markdown (`summary_report.md`):** Formatted tabular report for documentation and viewing.
- **Plain Text (`summary_report.txt`):** Fixed-width, ASCII-aligned audit report for human inspection.
