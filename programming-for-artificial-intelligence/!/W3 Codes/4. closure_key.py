#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:56:58 2026

@author: awais
"""

def api_client(api_key):
    
    def get_data(endpoint):
        print(f"Fetching from {endpoint} using key: {api_key}")
    return get_data

# The 'google_service' function now "carries" the key secretly
google_service = api_client("SECRET_123")
google_service("/maps")