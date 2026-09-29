#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:26:35 2026

@author: awais
"""

# Generator

def ucp_range(size):
    count = 0
    while count < size:
        print("generating: ", str(count))
        yield count
        count += 1
        

for i in ucp_range(100):
    print(i)