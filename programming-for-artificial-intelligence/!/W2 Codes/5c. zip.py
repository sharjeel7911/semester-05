#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:29:07 2026

@author: awais
"""
# a dictionary where the roll_no is the key, and the value is another dictionary containing the name and marks

names = ["Ali", "Sara", "Ahmed"]
roll_nos = [101, 102, 103]
marks = [85, 92, 78]


# The Pythonic "One-Liner"
student_db = {
    roll: {"name": name, "score": mark} 
    for name, roll, mark in zip(names, roll_nos, marks)
}

print(student_db)
# Output: {'name': 'Sara', 'score': 92}