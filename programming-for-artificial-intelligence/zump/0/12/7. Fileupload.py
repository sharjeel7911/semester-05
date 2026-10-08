#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:52:51 2026

@author: awais
"""

import requests
import os

def upload_analytical_file(filepath):
    # Using an open API testing service endpoint that accepts binary echo forms
    url = "https://httpbin.org/post"
    
    if not os.path.exists(filepath):
        return "File path invalid."
        
    # Open the file resource in strict Binary Read mode ('rb')
    # Using 'with' statements guarantees the file closes securely even if network calls throw errors
    with open(filepath, 'rb') as Target_File:
        # Structure the multipart payload configuration
        upload_payload = {
            'file': (os.path.basename(filepath), Target_File, 'application/octet-stream')
        }
        
        # Trigger transmission using the 'files=' parameter context
        response = requests.post(url, files=upload_payload)
        
    if response.status_code == 200:
        server_echo = response.json()
        return f"Upload Complete. Server recognized file size: {len(server_echo.get('files', {}).get('file', ''))} characters."
    else:
        return f"Upload failed with status code: {response.status_code}"

# --- Generating dummy file to showcase execution execution ---
dummy_path = "/media/Data/UCP/S26/Programming for AI/Notes/Week 12/flag.png"
with open(dummy_path, "wb") as f:
    f.write(b"\x93NUMPY\x01\x00_dummy_binary_payload_data_")

# --- Execution ---
upload_confirmation = upload_analytical_file(dummy_path)
print(upload_confirmation)

# Cleanup environment artifact
if os.path.exists(dummy_path):
    os.remove(dummy_path)