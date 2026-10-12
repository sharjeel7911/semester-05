"""
Integrity Manager - Calculates and verifies SHA-256 hashes for data integrity
"""

import hashlib
import json
import os
from pathlib import Path


class IntegrityManager:
    """Manages data integrity verification using SHA-256."""

    def __init__(self, hash_dir=None):
        """
        Initialize the integrity manager.

        Args:
            hash_dir: Directory to store hash files. Defaults to ~/usb-monitor/reports
        """
        if hash_dir is None:
            home = str(Path.home())
            hash_dir = os.path.join(home, "usb-monitor", "reports")

        self.hash_dir = hash_dir
        os.makedirs(self.hash_dir, exist_ok=True)

    def calculate_hash(self, file_path):
        """
        Calculate SHA-256 hash of a file.

        Args:
            file_path: Path to file to hash

        Returns:
            SHA-256 hash as hexadecimal string
        """
        sha256_hash = hashlib.sha256()

        try:
            with open(file_path, "rb") as f:
                # Read file in chunks to handle large files efficiently
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    def save_hash(self, file_path, hash_value=None):
        """
        Calculate hash of file and save it to a separate hash file.

        Args:
            file_path: Path to file to hash
            hash_value: Pre-calculated hash (optional). If None, calculate it.

        Returns:
            Path to saved hash file
        """
        if hash_value is None:
            hash_value = self.calculate_hash(file_path)

        if hash_value is None:
            return None

        # Create hash filename (e.g., activity_log.json.sha256)
        hash_filename = os.path.basename(file_path) + ".sha256"
        hash_file_path = os.path.join(self.hash_dir, hash_filename)

        # Save hash with metadata
        hash_data = {
            "file": file_path,
            "hash": hash_value,
            "algorithm": "SHA-256",
            "saved_at": datetime.now().isoformat()
            if "datetime" in globals()
            else str(os.path.getmtime(file_path)),
        }

        try:
            with open(hash_file_path, "w") as f:
                json.dump(hash_data, f, indent=2)
            return hash_file_path
        except IOError as e:
            print(f"Error saving hash file: {e}")
            return None

    def verify_integrity(self, file_path, stored_hash=None):
        """
        Verify that a file's hash matches the stored value.

        Args:
            file_path: Path to file to verify
            stored_hash: Expected hash value (or path to .sha256 file)

        Returns:
            Dictionary with verification results
        """
        current_hash = self.calculate_hash(file_path)

        if current_hash is None:
            return {"verified": False, "error": "Could not calculate hash"}

        # If stored_hash is a file path, read it
        if stored_hash and os.path.isfile(stored_hash):
            try:
                with open(stored_hash, "r") as f:
                    data = json.load(f)
                    stored_hash = data.get("hash")
            except (json.JSONDecodeError, IOError):
                return {"verified": False, "error": "Could not read hash file"}

        if stored_hash is None:
            return {"verified": False, "error": "No stored hash provided"}

        verified = current_hash == stored_hash
        return {
            "verified": verified,
            "current_hash": current_hash,
            "stored_hash": stored_hash,
            "file": file_path,
        }

    def get_hash_file_path(self, original_file_path):
        """Get the path where hash file should be saved."""
        hash_filename = os.path.basename(original_file_path) + ".sha256"
        return os.path.join(self.hash_dir, hash_filename)


# Import datetime at module level
from datetime import datetime
