"""
Activity Logger - Records USB events to JSON log file
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ActivityLogger:
    """Logs USB activity events with timestamps in JSON format."""

    def __init__(self, log_dir=None):
        """
        Initialize the activity logger.

        Args:
            log_dir: Directory to store logs. Defaults to ~/usb-monitor/reports
        """
        if log_dir is None:
            home = str(Path.home())
            log_dir = os.path.join(home, "usb-monitor", "reports")

        self.log_dir = log_dir
        self.log_file_path = os.path.join(log_dir, "activity_log.json")
        self.events = []

        # Create directory if it doesn't exist
        os.makedirs(self.log_dir, exist_ok=True)

        # Load existing events if log file exists
        self._load_existing_log()

    def _load_existing_log(self):
        """Load existing events from log file if it exists."""
        if os.path.exists(self.log_file_path):
            try:
                with open(self.log_file_path, "r") as f:
                    data = json.load(f)
                    self.events = data.get("events", [])
            except (json.JSONDecodeError, IOError):
                self.events = []

    def log_event(self, event_type, details):
        """
        Record a single event to the log.

        Args:
            event_type: Type of event (e.g., 'MONITORING_STARTED', 'USB_CONNECTED')
            details: Dictionary with event details

        Returns:
            The event dictionary that was logged
        """
        timestamp = datetime.now().isoformat()
        event = {"timestamp": timestamp, "event_type": event_type, "details": details}
        self.events.append(event)
        self._save_log()
        return event

    def _save_log(self):
        """Save all events to JSON file."""
        log_data = {
            "version": "1.0",
            "total_events": len(self.events),
            "last_updated": datetime.now().isoformat(),
            "events": self.events,
        }

        try:
            with open(self.log_file_path, "w") as f:
                json.dump(log_data, f, indent=2)
        except IOError as e:
            print(f"Error saving log file: {e}")

    def save_log_to_json(self):
        """Explicitly save log to JSON (calls _save_log internally)."""
        self._save_log()

    def get_log_file_path(self):
        """Return path to the current log file."""
        return self.log_file_path

    def get_all_events(self):
        """Return all logged events."""
        return self.events

    def get_event_count(self):
        """Return total number of logged events."""
        return len(self.events)

    def clear_log(self):
        """Clear all events (for testing only)."""
        self.events = []
        self._save_log()
