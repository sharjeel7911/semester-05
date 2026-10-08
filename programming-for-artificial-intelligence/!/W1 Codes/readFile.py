#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 09:02:13 2026

@author: awais
"""

with open('data.txt', 'r') as file:
    lines = file.readlines()

print(f"Stored {len(lines)} lines from file:")
print(lines)