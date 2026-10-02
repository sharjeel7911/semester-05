#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:23:02 2026

@author: awais
"""

import requests

def automated_session_pipeline():
    # We initialize a persistent session object
    # Think of this as opening a dedicated Chrome profile tab in code memory
    with requests.Session() as session:
        
        # 1. Define global headers that apply to EVERY request made by this session
        session.headers.update({
            "User-Agent": "UCP-AI-Bot/1.0",
            "Accept": "application/json"
        })
        
        print("--- Step 1: Simulating Login Action ---")
        # We tell httpbin to simulate dropping an authentication cookie named 'auth_token'
        login_url = "https://httpbin.org/cookies/set/auth_token/SECURE_HASHED_VAL_2026"
        session.get(login_url)
        
        print("Logged in successfully. Inspecting active session cookie jar:")
        print(session.cookies.get_dict())
        
        print("\n--- Step 2: Fetching Secure Protected Data ---")
        # This secure endpoint check relies on the 'auth_token' cookie set in Step 1.
        # Notice we don't pass the cookies or headers parameters here! 
        # The Session object handles it under the hood automatically.
        secure_data_url = "https://httpbin.org/cookies"
        response = session.get(secure_data_url)
        
        print("Data fetched seamlessly using retained state:")
        print(response.json())
        
    # Outside the 'with' block, the session closes, connection pool drops, and memory flushes
    print("\nSession safely closed.")

# --- Execution ---
automated_session_pipeline()