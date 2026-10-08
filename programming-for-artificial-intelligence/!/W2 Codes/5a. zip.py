#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:25:25 2026

@author: awais
"""

names = ["Ali", "Sara", "Ahmed", "Farhan"]
roll_nos = [101, 102, 103, 105]
marks = [85, 92, 78, 72]

combined = []
# for i in range(len(names)):
#     n = names[i]
#     r = roll_nos[i]
#     m = marks[i]

#     rec = (n, r, m)
#     combined.append(rec)


# for item in zip(roll_nos, names, marks, names):
#     print(item)

# Merging into a list of tuples
combined = list(zip(names, roll_nos, marks))

print(combined)
# Output: [('Ali', 101, 85), ('Sara', 102, 92), ('Ahmed', 103, 78)]