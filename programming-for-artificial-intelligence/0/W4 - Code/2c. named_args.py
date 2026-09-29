#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 01:19:13 2026

@author: awais
"""

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Order doesn't matter because we are naming them
result = calculate_bmi(height=1.75, weight=70)
print(f"The bmi is {result:.2f}")