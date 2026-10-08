#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:16:29 2026

@author: awais
"""
# Creating a dictionary
student = {
    "name": "Arsalan",
    "roll_no": "L1F23BSCS0123",
    "courses": ["ITC", "OOP", "MVC", "IML", "AI", "NLP"],
    "age" : 19
}

# Accessing a key value
# print(student)    # Output: Whole Record

# student["name"] = "Sara"

# print(student)    


student["cgpa"] = 3.8     # Adding a new key-value pair
# # Accessing whole record
# print(student)

# # Accessing each key without knowing how many keys and key names
for key, value in student.items():
    print(f"my val for {key} is {value}")
