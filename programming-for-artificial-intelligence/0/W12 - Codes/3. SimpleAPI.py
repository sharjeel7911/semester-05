#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:37:50 2026

@author: awais
"""

import requests

def get_coordinates_by_postal_code(postal_code, country="us"):
    # Target a public, unauthenticated geocoding API
    url = f"https://api.zippopotam.us/{country}/{postal_code}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # .json() automatically deserializes the string into a Python dict
        data = response.json()
        
        # Target specific nested attributes
        place_info = data["places"][0]
        return {
            "City": place_info["place name"],
            "State": place_info["state"],
            "Longitude": place_info["longitude"],
            "Latitude": place_info["latitude"]
        }
    else:
        return {"Error": "Invalid code or service unavailable"}

# --- Execution ---
location = get_coordinates_by_postal_code("90210")
print(f"Location Details: {location}")


# 90210, 33193, 11220