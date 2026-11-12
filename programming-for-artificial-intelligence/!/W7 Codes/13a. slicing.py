#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:06:43 2026

@author: awais
"""
import numpy as np

# --- Windowing ---
def get_window(signal, start, end):
    return signal[start:end]

data = np.arange(0, 100, 1) # Dummy signal
segment = get_window(data, 10, 20)
print(f"Data Segment: {segment}")

    