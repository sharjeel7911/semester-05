"""
Consent Manager - Handles user authorization before monitoring starts
"""

import json
import os
from pathlib import Path


class ConsentManager:
    """Manages consent from the user before USB monitoring begins."""

    CONSENT_MESSAGE = """
╔══════════════════════════════════════════════════════════════════════╗
║                    USB ACTIVITY MONITORING SYSTEM                    ║
║                   Educational Cybersecurity Project                  ║
╚══════════════════════════════════════════════════════════════════════╝

CONSENT NOTICE - PLEASE READ CAREFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This application will monitor USB device connections and disconnections.

WHAT WILL BE MONITORED:
  ✓ USB device connection events
  ✓ USB device disconnection events
  ✓ Date and time of events
  ✓ File copy operations from ~/Documents (Linux) or Documents (Windows)
  ✓ Activity log start/stop events

WHAT WILL NOT BE MONITORED:
  ✗ Keyboard input (keystrokes)
  ✗ Passwords or credentials
  ✗ Browser history or cookies
  ✗ Webcam or microphone
  ✗ Any other directories outside Documents

DATA STORAGE:
  • All logs saved to: ~/usb-monitor/reports/
  • Format: JSON (human-readable)
  • You can view and delete logs anytime
  • Data is stored locally only

MONITORING SCOPE:
  • This is a LOCAL, EDUCATIONAL application
  • Runs only on YOUR computer
  • Does NOT send data anywhere
  • You can stop at any time
  • Fully transparent and consent-based

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do you CONSENT to USB activity monitoring?

Type your choice:
  YES    - Start monitoring (must type exactly "YES")
  NO     - Exit without monitoring (must type exactly "NO")
"""

    def __init__(self):
        """Initialize consent manager."""
        self.user_consented = False
        self.consent_record_path = os.path.join(
            str(Path.home()), "usb-monitor", "reports", "consent_record.json"
        )
        os.makedirs(os.path.dirname(self.consent_record_path), exist_ok=True)

    def display_consent_screen(self):
        """
        Display consent notice and get user approval.

        Returns:
            True if user consented, False otherwise
        """
        print(self.CONSENT_MESSAGE)

        while True:
            user_input = input("\nYour choice (YES/NO): ").strip().upper()

            if user_input == "YES":
                self.user_consented = True
                self._record_consent(True)
                print("\n✓ Consent recorded. Starting monitoring...\n")
                return True
            elif user_input == "NO":
                self.user_consented = False
                self._record_consent(False)
                print("\n✗ Monitoring cancelled. Exiting application.\n")
                return False
            else:
                print("⚠ Invalid input. Please type YES or NO.")

    def _record_consent(self, consented):
        """Record consent decision to file."""
        from datetime import datetime

        consent_data = {
            "consented": consented,
            "timestamp": datetime.now().isoformat(),
            "decision": "APPROVED" if consented else "DENIED",
        }

        try:
            with open(self.consent_record_path, "w") as f:
                json.dump(consent_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save consent record: {e}")

    def get_consent_status(self):
        """Return whether user has given consent."""
        return self.user_consented

    def was_consent_given_before(self):
        """Check if consent was given in a previous run."""
        if os.path.exists(self.consent_record_path):
            try:
                with open(self.consent_record_path, "r") as f:
                    data = json.load(f)
                    return data.get("consented", False)
            except (json.JSONDecodeError, IOError):
                return False
        return False
