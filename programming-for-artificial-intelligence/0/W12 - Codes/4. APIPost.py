#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:41:53 2026

@author: awais
"""

import requests

def create_mock_student_record(student_id, name, final_grade):
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Pack the parameters inside a native Python dictionary
    payload = {
        "userId": student_id,
        "title": name,
        "body": f"Enrolled student recorded with final raw performance index: {final_grade}"
    }
    
    # Send an HTTP POST request. The 'json=' argument sets headers to application/json automatically
    response = requests.post(url, json=payload)
    
    print(f"HTTP Status Received: {response.status_code} (Created)")
    return response.json()

# --- Execution ---
new_record = create_mock_student_record(student_id=14, name="Aisha Ahmed", final_grade=18)
print(f"Server Confirmation Payload: {new_record}")