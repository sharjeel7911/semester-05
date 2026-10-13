# Consent-Based USB Activity Monitoring System

An educational defensive cybersecurity tool developed in Python to safely monitor USB storage device connection/disconnection events with explicit user consent, cryptographic integrity verification (SHA-256), and auditable reporting.

---

## 🚀 Quickstart with `uv`

This project uses [`uv`](https://docs.astral.sh/uv/) for Python packaging and virtual environment management.

### 1. Prerequisites
Ensure `uv` is installed on your Linux system:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Environment Setup
Install the project dependencies and sync the virtual environment:
```bash
uv sync
```

### 3. Run the Monitoring System
Start the USB monitor:
```bash
uv run python monitor/main.py
```
1. Read the consent screen and type `YES` to start monitoring.
2. Plug in or unplug your USB storage drives to see live detection.
3. Press `Ctrl+C` to gracefully terminate monitoring, compute the SHA-256 hash, and generate reports.

### 4. Run Stage 8 Data Integrity / Tamper Demo
Demonstrate that modifying a single byte in the log invalidates its cryptographic SHA-256 checksum:
```bash
uv run python monitor/main.py --demo-tamper
```

---

## 📁 Output Directory (`reports/`)

All generated artifacts are saved to `reports/`:
- `consent_record.json`: Timestamped user consent approval record.
- `activity_log.json`: Structured event log containing USB hardware and storage metadata.
- `activity_log.json.sha256`: SHA-256 cryptographic digest of the activity log.
- `summary_report.txt`: Clean, human-readable ASCII audit report.
- `summary_report.md`: Markdown summary report with event tables.

---

## 📑 Detailed Documentation

For a comprehensive explanation of the system architecture, how the Linux kernel and `udev` capture USB events, ethical boundaries, and Windows implementation status, see:
- [System Architecture & Linux Mechanism Documentation](documentation/SYSTEM_DOCUMENTATION.md)
