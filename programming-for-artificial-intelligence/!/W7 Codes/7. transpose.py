#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:27:35 2026

@author: awais
"""

import numpy as np

# Swap rows and columns
original = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# original.shape is (2, 3)

transposed = original.T 
# transposed.shape is (3, 2)