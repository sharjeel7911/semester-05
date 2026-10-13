"""
User Interface - Terminal-based beautiful UI using Pillow-inspired layouts
"""

import json
import os
from datetime import datetime
from pathlib import Path


class UserInterface:
    """Terminal-based user interface for the monitoring system."""

    # ANSI color codes
    COLORS = {
        "HEADER": "\033[95m",
        "BLUE": "\033[94m",
        "CYAN": "\033[96m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "RESET": "\033[0m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
    }

    def __init__(self):
        """Initialize UI."""
        pass

    @staticmethod
    def print_header(title):
        """Print a formatted header."""
        color = UserInterface.COLORS
        print(f"\n{color['BOLD']}{color['CYAN']}")
        print("╔" + "═" * 78 + "╗")
        print(f"║ {title:<76} ║")
        print("╚" + "═" * 78 + "╝")
        print(color["RESET"])

    @staticmethod
    def print_section(title):
        """Print a section header."""
        color = UserInterface.COLORS
        print(f"\n{color['BOLD']}{color['BLUE']}━━━ {title} ━━━{color['RESET']}")

    @staticmethod
    def print_success(message):
        """Print success message."""
        color = UserInterface.COLORS
        print(f"{color['GREEN']}✓ {message}{color['RESET']}")

    @staticmethod
    def print_error(message):
        """Print error message."""
        color = UserInterface.COLORS
        print(f"{color['RED']}✗ {message}{color['RESET']}")

    @staticmethod
    def print_warning(message):
        """Print warning message."""
        color = UserInterface.COLORS
        print(f"{color['YELLOW']}⚠ {message}{color['RESET']}")

    @staticmethod
    def print_info(message):
        """Print info message."""
        color = UserInterface.COLORS
        print(f"{color['CYAN']}ℹ {message}{color['RESET']}")

    @staticmethod
    def print_status_line(label, value, width=40):
        """Print a formatted status line."""
        color = UserInterface.COLORS
        line = f"  {label:<20} : {value}"
        print(line)

    @staticmethod
    def display_activity_report(events, log_file_path, hash_file_path=None, report_dir=None):
        """
        Display and save a formatted activity report.

        Args:
            events: List of event dictionaries
            log_file_path: Path to log file
            hash_file_path: Path to hash file
            report_dir: Directory where reports should be saved
        """
        color = UserInterface.COLORS
        UserInterface.print_header("ACTIVITY REPORT")

        report_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{color['BOLD']}Summary:{color['RESET']}")
        UserInterface.print_status_line("Total Events", str(len(events)))
        UserInterface.print_status_line("Report Generated", report_time_str)
        UserInterface.print_status_line("Log File", log_file_path)

        if hash_file_path:
            UserInterface.print_status_line("Hash File", hash_file_path)

        print(f"\n{color['BOLD']}Event Details:{color['RESET']}")
        print(f"{'Timestamp':<24} {'Event Type':<22} {'Details'}")
        print("─" * 80)

        report_lines = [
            "# USB Activity Monitoring Report",
            f"- **Generated:** {report_time_str}",
            f"- **Total Events:** {len(events)}",
            f"- **Log File:** `{log_file_path}`",
            f"- **Hash File:** `{hash_file_path or 'N/A'}`",
            "",
            "## Recorded Events",
            "| Timestamp | Event Type | Details |",
            "| :--- | :--- | :--- |",
        ]

        # Generate human-readable summary text report (.txt)
        txt_report_lines = [
            "=" * 78,
            "                   USB ACTIVITY MONITORING AUDIT REPORT",
            "=" * 78,
            f"Generated At : {report_time_str}",
            f"Total Events : {len(events)}",
            f"Log File     : {log_file_path}",
            f"Hash File    : {hash_file_path or 'N/A'}",
            "-" * 78,
            f"{'TIMESTAMP':<22} | {'EVENT TYPE':<20} | {'DETAILS'}",
            "-" * 78,
        ]

        for event in events:
            timestamp = event.get("timestamp", "N/A")[:19]
            event_type = event.get("event_type", "UNKNOWN")
            details = event.get("details", {})

            if "vendor" in details or "model" in details:
                summary_str = f"{details.get('vendor', 'Unknown')} {details.get('model', 'Unknown')}"
                if details.get("serial") and details.get("serial") != "Unknown":
                    summary_str += f" (S/N: {details.get('serial')})"
                if details.get("storage_volumes"):
                    vols = [v.get("node") for v in details["storage_volumes"] if v.get("node")]
                    if vols:
                        summary_str += f" [Volumes: {', '.join(vols)}]"
            else:
                summary_str = ", ".join(f"{k}: {v}" for k, v in details.items())

            print(f"{timestamp:<24} {event_type:<22} {summary_str[:50]}")

            report_lines.append(f"| {timestamp} | {event_type} | {summary_str} |")
            txt_report_lines.append(f"{timestamp:<22} | {event_type:<20} | {summary_str}")

        txt_report_lines.append("=" * 78)
        print()

        # Save report files to disk
        if report_dir is None:
            report_dir = os.path.dirname(log_file_path)

        report_file_path = os.path.join(report_dir, "summary_report.md")
        txt_file_path = os.path.join(report_dir, "summary_report.txt")
        try:
            with open(report_file_path, "w") as f:
                f.write("\n".join(report_lines) + "\n")
            with open(txt_file_path, "w") as f:
                f.write("\n".join(txt_report_lines) + "\n")
            UserInterface.print_success(f"Reports saved: summary_report.md & summary_report.txt")
            return report_file_path
        except IOError as e:
            UserInterface.print_warning(f"Could not save reports: {e}")
            return None

    @staticmethod
    def display_hash_verification(verification_result):
        """
        Display hash verification result.

        Args:
            verification_result: Dictionary with verification data
        """
        UserInterface.print_section("Hash Verification Result")

        if verification_result.get("verified"):
            UserInterface.print_success("File integrity verified!")
        else:
            UserInterface.print_error("File integrity check failed!")

        print(f"  File: {verification_result.get('file', 'N/A')}")
        print(f"  Current Hash:  {verification_result.get('current_hash', 'N/A')}")
        print(f"  Stored Hash:   {verification_result.get('stored_hash', 'N/A')}")
        print()

    @staticmethod
    def display_monitoring_status(is_monitoring, connected_devices):
        """
        Display current monitoring status.

        Args:
            is_monitoring: Boolean monitoring status
            connected_devices: List of connected USB devices
        """
        UserInterface.print_section("Monitoring Status")

        status = "ACTIVE" if is_monitoring else "INACTIVE"
        status_color = (
            UserInterface.COLORS["GREEN"]
            if is_monitoring
            else UserInterface.COLORS["RED"]
        )

        print(f"  Status: {status_color}{status}{UserInterface.COLORS['RESET']}")
        print(f"  Connected USB Devices: {len(connected_devices)}")

        for device in connected_devices:
            vendor = device.get("vendor", "Unknown")
            model = device.get("model", "Unknown")
            print(f"    • {vendor} {model}")
        print()
