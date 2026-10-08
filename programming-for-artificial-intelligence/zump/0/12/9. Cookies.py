#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:20:36 2026

@author: awais
"""

import requests

def manage_cookies_explicitly():
    # An endpoint designed to echo back whatever cookies you send it
    url = "https://httpbin.org/cookies"
    
    # 1. Setting and Sending custom cookies to the server
    my_cookies = {
        "session_id": "987654321_AI_STUDENT",
        "has_accepted_terms": "true"
    }
    
    response = requests.get(url, cookies=my_cookies)
    print("--- Server Echoed Our Cookies Back ---")
    print(response.json())
    
    # 2. Getting cookies dropped by a server
    # Let's visit an endpoint that forces the server to issue a fresh cookie to us
    cookie_setter_url = "https://httpbin.org/cookies/set/theme/dark"
    response_with_new_cookie = requests.get(cookie_setter_url)
    
    print("\n--- Capturing Incoming Server Cookies ---")
    # response.cookies behaves like a dictionary container called a RequestsCookieJar
    dropped_cookies = response_with_new_cookie.cookies
    for cookie_name, cookie_value in dropped_cookies.items():
        print(f"Cookie Saved -> Name: {cookie_name} | Value: {cookie_value}")

# --- Execution ---
manage_cookies_explicitly()