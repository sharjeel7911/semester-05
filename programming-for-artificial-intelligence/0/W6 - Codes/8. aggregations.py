#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:30:28 2026

@author: awais
"""

import numpy as np


matrix = np.array([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 6]])

# Sum of EVERYTHING
print("Sum", np.sum(matrix)) # 10

# Sum along rows (Vertical)
print("Axis 0 Sum", np.sum(matrix, axis=0))

# Sum along columns (Horizontal)
print("Axis 1 Sum", np.sum(matrix, axis=1))


print("Axis -1 Sum", np.sum(matrix, axis=-1))