# PROMPT: Consent-Based USB Activity Monitoring System

You are a Senior Cyber Security Instructor and Defensive Systems Engineer. Build an educational, defensive, consent-based USB activity monitoring application in Python using `uv` for project and package management.

The tool must monitor USB device connection and disconnection events safely, record rich hardware and storage metadata, verify data integrity using cryptographic SHA-256 digests, and generate structured and human-readable audit reports.

---

## 1. Project Objectives & Core Requirements

1. **User Consent Gate (`ConsentManager`):**
   - Must display a clear terminal consent notice detailing what is monitored and what is strictly prohibited.
   - Monitoring must NOT begin unless the user explicitly inputs `YES`.
   - Record the consent decision with a timestamp to `reports/consent_record.json`.

2. **USB Detection & Extraction (`UsbMonitor`):**
   - **Linux Platform:** Detect device insertion and removal asynchronously using `pyudev` and netlink sockets.
   - **Prevent Duplicate Events:** Filter netlink messages strictly by `device.device_type == "usb_device"`, ignoring `usb_interface` sub-devices so that one plug/unplug produces exactly one event.
   - **Rich Hardware Metadata:** Extract `vendor`, `model`, `vendor_id` (`ID_VENDOR_ID`), `model_id` (`ID_MODEL_ID`), `serial` (`ID_SERIAL_SHORT`), `bus_num`, `dev_num`, `speed`, and `usb_driver`.
   - **Storage & Volume Correlation:** Inspect the `block` subsystem to identify if the USB is a mass storage device (`ID_USB_INTERFACES` contains `:08`). Add a short delay (0.5s) to allow SCSI block nodes to settle, then extract block node path (`/dev/sdX1`), partition type, filesystem type (`ID_FS_TYPE`), filesystem label (`ID_FS_LABEL`), UUID (`ID_FS_UUID`), and active mount point from `/proc/mounts`.
   - **Windows Platform:** Provide a graceful placeholder stub indicating Windows support is pending.

3. **Activity Logging (`ActivityLogger`):**
   - Maintain an in-memory event stream and persist it to `reports/activity_log.json`.
   - Record events for `MONITORING_STARTED`, `USB_CONNECTED`, `USB_DISCONNECTED`, and `MONITORING_STOPPED`.
   - Each event must contain an ISO-8601 timestamp, event type, and detailed payload.

4. **Cryptographic Integrity Verification (`IntegrityManager`):**
   - Compute the SHA-256 hash digest of `reports/activity_log.json` by streaming chunks (4096 bytes).
   - Save the hash digest with metadata to `reports/activity_log.json.sha256`.
   - Provide a verification function that recalculates the hash and compares it against the stored digest.

5. **Multi-Format Audit Reporting (`UserInterface`):**
   - All reports must be saved directly inside `reports/`:
     - `reports/activity_log.json`: Machine-readable structured log.
     - `reports/activity_log.json.sha256`: SHA-256 digest file.
     - `reports/summary_report.md`: Markdown summary table of recorded activity.
     - `reports/summary_report.txt`: Fixed-width, clean, human-readable ASCII audit report.

6. **Interactive CLI & Tamper Demonstration (`main.py`):**
   - Handle graceful shutdown via `SIGINT` (Ctrl+C).
   - Include a `--demo-tamper` flag (Stage 8) that verifies an authentic log file, injects an unauthorized byte/modification into `activity_log.json`, demonstrates the SHA-256 verification failure, and restores the original file.

---

## 2. Strict Privacy & Ethical Boundaries

The application is defensive and educational. It must NOT:
- Steal passwords, capture keystrokes, or collect clipboard contents.
- Collect browser history, cookies, or saved sessions.
- Access webcam, microphone, or user documents outside of explicit educational scope.
- Hide processes from the user, bypass system security, or execute binary payloads from the USB.
- Exfiltrate or transmit data over the network.

---

## 3. Directory & Package Structure

Organize the repository cleanly:

```text
usb-monitor/
├── documentation/
│   ├── SYSTEM_DOCUMENTATION.md
│   └── PROMPT.md
├── monitor/
│   ├── __init__.py
│   ├── activity_logger.py
│   ├── consent_manager.py
│   ├── integrity_manager.py
│   ├── ui.py
│   ├── usb_monitor.py
│   └── main.py
├── reports/
│   ├── activity_log.json
│   ├── activity_log.json.sha256
│   ├── consent_record.json
│   ├── summary_report.md
│   └── summary_report.txt
├── pyproject.toml
└── README.md
```

### Dependencies (`pyproject.toml`)
Manage dependencies using `uv`:
- Python: `>=3.11`
- Dependencies: `pyudev>=0.24.5`, `pillow>=12.3.0`
- Build system: `hatchling`

---

## 4. Execution Commands (using `uv`)

- Sync project dependencies:
  ```bash
  uv sync
  ```
- Run monitoring system:
  ```bash
  uv run python monitor/main.py
  ```
- Run Stage 8 data integrity tamper demonstration:
  ```bash
  uv run python monitor/main.py --demo-tamper
  ```
