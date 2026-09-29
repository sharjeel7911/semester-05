#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:22:43 2026

@author: awais
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise Math
print(a + b)  # [5, 7, 9]
print(a * b)  # [4, 10, 18]

# Scalar Operations
print(a+5)
print(a ** 2) # [1, 4, 9] (Square each element)


b = np.append(b, 10)

try:
    print(a + b)
except Exception as e:
    print (e)
