#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:51:52 2026

@author: awais
"""

import requests
import xml.etree.ElementTree as ET

def parse_xml_weather_feed():
    # Accessing an open test XML endpoint
    url = "https://www.w3schools.com/xml/note.xml"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the raw text string into an XML Node Element Tree
        root = ET.fromstring(response.text)
        
        # Read properties via specific component tags
        note_to = root.find('to').text
        note_from = root.find('from').text
        note_heading = root.find('heading').text
        note_body = root.find('body').text
        
        return {
            "Recipient": note_to,
            "Sender": note_from,
            "Subject": note_heading,
            "Message": note_body
        }
    return None

# --- Execution ---
xml_details = parse_xml_weather_feed()
print(f"Decoded XML Structure: {xml_details}")