#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:02:57 2026

@author: awais
"""
import numpy as np


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stack vertically (Result is 4x2)
v_stack = np.concatenate((a, b), axis=0)

# Stack horizontally (Result is 2x4)
h_stack = np.concatenate((a, b), axis=1)