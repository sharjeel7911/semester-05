#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:57:21 2026

@author: awais
"""

import numpy as np

# From a list (1D)
arr_1d = np.array([10, 20, 30])

# 2D Array (Matrix) - Think of it as a list of lists
matrix = np.array([[1, 2], [3, 4], [5, 6]]) 

# ND Array (3D Example: 2 layers, 3 rows, 2 columns)
# Common in Medical Imaging (CT scans are 3D)
arr_3d = np.zeros((2, 3, 2)) 

print(arr_1d)