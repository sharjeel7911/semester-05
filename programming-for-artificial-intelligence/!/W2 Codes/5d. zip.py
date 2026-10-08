#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:30:59 2026

@author: awais
"""

# lists of different sizes

# names = ["Ali", "Sara", "Ahmed"]
# roll_nos = [101, 102, 103]
# marks = [85, 92, 78]

names = ["Ali", "Sara", "Awais", "Salman"]
rolls = [101, 102, 105, 111]
marks = [55, 65, 75]
combined = list(zip(names, rolls, marks))

print(combined)

# zip will only produce TWO pairs. 
# Roll 103 is simply ignored.