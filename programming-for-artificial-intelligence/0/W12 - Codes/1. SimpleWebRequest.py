#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:22:48 2026

@author: awais
"""

import requests
from bs4 import BeautifulSoup

def fetch_web_title(url):
    # Send a standard HTTP GET request
    response = requests.get(url)
    
    # 200 OK means success
    if response.status_code == 200:
        # Feed raw HTML into the parser
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the text within the <title> tag
        page_title = soup.title.string if soup.title else "No title found"
        return page_title
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

# --- Execution ---
target_url = "https://example.com"
print(f"Page Title: {fetch_web_title(target_url)}")