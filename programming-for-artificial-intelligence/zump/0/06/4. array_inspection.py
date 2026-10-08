#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:21:37 2026

@author: awais
"""

import numpy as np

# A 2D Matrix (3 rows, 2 columns)
data = np.array([[10, 20], [30, 40], [50, 60]])

print(f"Shape: {data.shape}") # (3, 2)
print(f"Size:  {data.size}")  # 6
print(f"Dims:  {data.ndim}")  # 2
print(f"Type:  {data.dtype}") # int64 (on most systems)