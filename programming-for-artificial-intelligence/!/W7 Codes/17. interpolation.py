#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 04:24:48 2026

@author: awais
"""
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


# --- Calling ---
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 5, 5]) # Sparse data

# Create a cubic spline interpolation function
f_cubic = interp1d(x, y, kind='cubic')

x_new = np.linspace(0, 4,10) # 10 points instead of 4
y_smooth = f_cubic(x_new)

print(f"Smoothed points: {y_smooth.round(2)}")

plt.plot(x,y)
plt.plot(x_new, y_smooth)