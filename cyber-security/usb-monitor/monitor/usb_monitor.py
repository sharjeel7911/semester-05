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

                action = device.action
                device_info = {
                    "device_name": device.device_node or "Unknown",
                    "device_path": device.device_path,
                    "vendor": device.get("ID_VENDOR", "Unknown"),
                    "model": device.get("ID_MODEL", "Unknown"),
                    "serial": device.get("ID_SERIAL", "Unknown"),
                }

                if action == "add":
                    self.connected_devices[device.device_path] = device_info
                    if self.callback:
                        self.callback("USB_CONNECTED", device_info)

                elif action == "remove":
                    if device.device_path in self.connected_devices:
                        del self.connected_devices[device.device_path]
                    if self.callback:
                        self.callback("USB_DISCONNECTED", device_info)

        except Exception as e:
            print(f"Error in USB monitoring: {e}")
            self.is_monitoring = False

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
