"""
USB Monitor - Detects USB device connections and disconnections
"""

import platform
import sys
import threading


class UsbMonitor:
    """Monitors USB device connection/disconnection events."""

    def __init__(self, callback=None):
        """
        Initialize USB monitor.

        Args:
            callback: Function to call when USB event occurs
                     callback(event_type, device_info)
        """
        self.is_monitoring = False
        self.connected_devices = {}
        self.callback = callback
        self.monitor_thread = None
        self.system = platform.system()

    def start_monitoring(self):
        """Start listening for USB events."""
        if self.is_monitoring:
            print("⚠ Already monitoring")
            return False

        self.is_monitoring = True

        if self.system == "Linux":
            self._start_monitoring_linux()
        elif self.system == "Windows":
            self._start_monitoring_windows()
        else:
            print(f"⚠ USB monitoring not supported on {self.system}")
            self.is_monitoring = False
            return False

        return True

    def _start_monitoring_linux(self):
        """Start monitoring on Linux using pyudev."""
        try:
            import pyudev
        except ImportError:
            print("Error: pyudev not installed. Run: pip install pyudev")
            self.is_monitoring = False
            return

        # Run monitoring in background thread
        self.monitor_thread = threading.Thread(target=self._monitor_linux, daemon=True)
        self.monitor_thread.start()

    def _monitor_linux(self):
        """Background thread for Linux USB monitoring."""
        try:
            import pyudev

            context = pyudev.Context()
            monitor = pyudev.Monitor.from_netlink(context)
            monitor.filter_by(subsystem="usb")

            print("✓ USB monitoring started (Linux)")

            for device in iter(monitor.poll, None):
                if not self.is_monitoring:
                    break

                # Filter strictly for physical USB devices, ignoring interface sub-devices
                # which cause duplicate connect/disconnect events
                if device.device_type != "usb_device":
                    continue

                action = device.action
                device_info = self._extract_device_info(context, device)

                if action == "add":
                    self.connected_devices[device.device_path] = device_info
                    if self.callback:
                        self.callback("USB_CONNECTED", device_info)

                elif action == "remove":
                    # Get previously stored info if available
                    cached_info = self.connected_devices.pop(device.device_path, device_info)
                    if self.callback:
                        self.callback("USB_DISCONNECTED", cached_info)

        except Exception as e:
            print(f"Error in USB monitoring: {e}")
            self.is_monitoring = False

    def _extract_device_info(self, context, device):
        """Extract rich metadata for USB device and its storage partitions."""
        import time

        info = {
            "device_name": device.device_node or "Unknown",
            "device_path": device.device_path,
            "vendor": device.get("ID_VENDOR_FROM_DATABASE") or device.get("ID_VENDOR") or "Unknown",
            "model": device.get("ID_MODEL_FROM_DATABASE") or device.get("ID_MODEL") or "Unknown",
            "vendor_id": device.get("ID_VENDOR_ID", "Unknown"),
            "model_id": device.get("ID_MODEL_ID", "Unknown"),
            "serial": device.get("ID_SERIAL_SHORT") or device.get("ID_SERIAL") or "Unknown",
            "bus_num": device.get("BUSNUM", "Unknown"),
            "dev_num": device.get("DEVNUM", "Unknown"),
            "speed": device.get("SPEED", "Unknown"),
            "usb_driver": device.get("DRIVER", "Unknown"),
            "usb_interfaces": device.get("ID_USB_INTERFACES", "Unknown"),
            "is_storage": False,
            "storage_volumes": [],
        }

        # Check interface class: 08 is Mass Storage
        interfaces = str(device.get("ID_USB_INTERFACES", ""))
        driver = str(device.get("DRIVER", ""))
        if ":08" in interfaces or "storage" in driver.lower():
            info["is_storage"] = True

        # Give the kernel 0.5s to create SCSI block device nodes upon insertion
        time.sleep(0.5)

        # Check associated block storage devices / partitions under this USB device
        try:
            for block_dev in context.list_devices(subsystem="block"):
                # Check if this block device path is a descendant of the USB device path
                if block_dev.device_path.startswith(device.device_path):
                    info["is_storage"] = True
                    vol_info = {
                        "node": block_dev.device_node,
                        "type": block_dev.device_type,  # disk or partition
                        "fs_type": block_dev.get("ID_FS_TYPE", "Unknown"),
                        "fs_label": block_dev.get("ID_FS_LABEL", "None"),
                        "fs_uuid": block_dev.get("ID_FS_UUID", "None"),
                        "mount_point": self._get_mount_point(block_dev.device_node),
                    }
                    info["storage_volumes"].append(vol_info)
        except Exception:
            pass

        return info

    def _get_mount_point(self, device_node):
        """Find mount point for a block device node if mounted."""
        if not device_node:
            return None
        try:
            with open("/proc/mounts", "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2 and parts[0] == device_node:
                        return parts[1]
        except Exception:
            pass
        return None

    def _start_monitoring_windows(self):
        """Start monitoring on Windows (placeholder)."""
        print("⚠ Windows USB monitoring not yet fully implemented")
        print("  (Requires win32api - install with: pip install pywin32)")
        self.is_monitoring = False

    def stop_monitoring(self):
        """Stop listening for USB events."""
        self.is_monitoring = False
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=2)
        print("✓ USB monitoring stopped")

    def get_connected_devices(self):
        """Return list of currently connected USB devices."""
        return list(self.connected_devices.values())

    def is_monitoring_active(self):
        """Return whether monitoring is currently active."""
        return self.is_monitoring
