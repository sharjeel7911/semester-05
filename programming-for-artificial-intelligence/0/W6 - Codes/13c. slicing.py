#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:10:02 2026

@author: awais
"""

import numpy as np


# --- Outlier Removal (ML Cleaning) ---
def clip_outliers(data):
    mean, std = np.mean(data), np.std(data)
    # Masking to replace values outside 2 standard deviations
    data[np.abs(data - mean) > 2 * std] = mean
    return data

sale_price = np.array([10, 12, 11, 120, 10, 11]) # 120 is a glitch
cleaned = clip_outliers(sale_price)
print(f"Cleaned Pricing: {cleaned}")