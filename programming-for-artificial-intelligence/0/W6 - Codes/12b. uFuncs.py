#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:53:42 2026

@author: awais
"""

import numpy as np


# --- Log-Transformation (Image Processing) ---
def log_transform(image_pixels):
    # Common in X-ray enhancement to expand dark pixels
    return np.log1p(image_pixels) 

xray_patch = np.array([10, 50, 100, 255])
enhanced = log_transform(xray_patch)
print(f"Log Enhanced: {enhanced}")

