#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:15:16 2026

@author: awais
"""

import requests

def fetch_with_custom_headers():
    url = "https://httpbin.org/headers"
    
    # Servers block scripts that use Python's default User-Agent ("python-requests/2.X.X")
    response = requests.get(url)
    print(response.json())
    # We override it to look like a standard Google Chrome browser on Windows
    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "X-Custom-Instructor-Token": "UCP-AI-Class-2026"  # Creating our own custom tracking header
    }
    
    response = requests.get(url, headers=custom_headers)
    
    print("--- 1. Request Headers Recognized by Server ---")
    print(response.json())
    
    print("\n--- 2. Metadata Returned from Server (Response Headers) ---")
    # Response headers behave exactly like a Python dictionary (case-insensitive keys)
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"Server Software: {response.headers.get('Server')}")

# --- Execution ---
fetch_with_custom_headers()