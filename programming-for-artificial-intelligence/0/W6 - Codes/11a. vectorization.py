#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:44:48 2026

@author: awais
"""

import numpy as np

# Signal Gain ---
def apply_gain(signal, factor):
    return signal * factor

raw_signal = np.array([0.1, 0.2, 0.5, 0.1])
amplified = apply_gain(raw_signal, 10)
print(f"Amplified: {amplified}") # [1. 2. 5. 1.]

