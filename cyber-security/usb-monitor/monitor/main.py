"""
USB Activity Monitoring System - Main Entry Point
Educational Cybersecurity Project
"""

import os
import signal
import sys
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from monitor.activity_logger import ActivityLogger
from monitor.consent_manager import ConsentManager
from monitor.integrity_manager import IntegrityManager
from monitor.ui import UserInterface
from monitor.usb_monitor import UsbMonitor


class USBMonitorApp:
    """Main application class."""

    def __init__(self):
        """Initialize the application."""
        self.consent_manager = ConsentManager()
        self.activity_logger = None
        self.usb_monitor = None
        self.integrity_manager = None
        self.is_running = True

    def handle_usb_event(self, event_type, device_info):
        """
        Callback for USB events.

        Args:
            event_type: Type of event (USB_CONNECTED, USB_DISCONNECTED)
            device_info: Dictionary with device information
        """
        self.activity_logger.log_event(event_type, device_info)

        if event_type == "USB_CONNECTED":
            UserInterface.print_success(
                f"USB Connected: {device_info.get('vendor', 'Unknown')} "
                f"{device_info.get('model', 'Unknown')}"
            )
        elif event_type == "USB_DISCONNECTED":
            UserInterface.print_warning(
                f"USB Disconnected: {device_info.get('vendor', 'Unknown')}"
            )

    def handle_interrupt(self, signum, frame):
        """Handle Ctrl+C gracefully."""
        print("\n")
        UserInterface.print_warning("Interrupt signal received...")
        self.is_running = False

    def run(self):
        """Run the application."""
        # Display header
        UserInterface.print_header("USB ACTIVITY MONITORING SYSTEM")
        print("Educational Cybersecurity Project\n")

        # Get consent
        if not self.consent_manager.display_consent_screen():
            return

        # Initialize components
        self.activity_logger = ActivityLogger()
        self.usb_monitor = UsbMonitor(callback=self.handle_usb_event)
        self.integrity_manager = IntegrityManager()

        # Log monitoring start
        self.activity_logger.log_event(
            "MONITORING_STARTED",
            {"reason": "User consented", "application": "USB-Monitor v0.1.0"},
        )

        UserInterface.print_success("Monitoring initialized")
        UserInterface.print_info(
            f"Logs will be saved to: {self.activity_logger.get_log_file_path()}"
        )

        # Start USB monitoring
        if not self.usb_monitor.start_monitoring():
            UserInterface.print_error("Failed to start USB monitoring")
            return

        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.handle_interrupt)

        # Main loop
        UserInterface.print_section("Monitoring Active")
        print("Press Ctrl+C to stop monitoring and generate report...\n")

        try:
            while self.is_running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.is_running = False

        # Shutdown
        self._shutdown()

    def _shutdown(self):
        """Gracefully shutdown the application."""
        UserInterface.print_section("Shutting Down")

        # Stop monitoring
        if self.usb_monitor:
            self.usb_monitor.stop_monitoring()

        # Log monitoring stop
        self.activity_logger.log_event(
            "MONITORING_STOPPED", {"reason": "User stopped monitoring"}
        )

        # Save log
        self.activity_logger.save_log_to_json()
        log_path = self.activity_logger.get_log_file_path()
        UserInterface.print_success(f"Activity log saved to: {log_path}")

        # Calculate and save hash
        hash_value = self.integrity_manager.calculate_hash(log_path)
        hash_file = self.integrity_manager.save_hash(log_path, hash_value)
        UserInterface.print_success(f"Hash saved to: {hash_file}")

        # Display report
        events = self.activity_logger.get_all_events()
        UserInterface.display_activity_report(events, log_path, hash_file)

        # Verify integrity
        verification = self.integrity_manager.verify_integrity(log_path, hash_file)
        UserInterface.display_hash_verification(verification)

        UserInterface.print_success("Application closed successfully")
        print()


def main():
    """Entry point."""
    try:
        app = USBMonitorApp()
        app.run()
    except Exception as e:
        UserInterface.print_error(f"Fatal error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
