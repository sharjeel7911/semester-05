#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:27:40 2026

@author: awais
"""

names = ["Ali", "Sara", "Ahmed"]
roll_nos = [101, 102, 103]
marks = [85, 92, 78]

# for n, r, m in zip(names, roll_nos, marks):
#     print(f"Student {n} (ID: {r}) scored {m} marks.")


for x in zip(names, roll_nos, marks):
    print(x)
    print(f"Student {x[0]} (ID: {x[1]}) scored {x[2]} marks.")