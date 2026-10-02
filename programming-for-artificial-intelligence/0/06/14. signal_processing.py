#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:13:04 2026

@author: awais
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


def clean_ecg(noisy_signal):
    # Create a Butterworth low-pass filter
    # b, a are filter coefficients (numerator/denominator)
    b, a = signal.butter(4, 0.2, btype='low')
    return signal.filtfilt(b, a, noisy_signal)

# --- Calling ---
# Simulating a noisy 100Hz signal
t = np.linspace(0, 1, 100)
noise = np.random.normal(0, 0.5, 100)
raw_ecg = np.sin(5 * 2 * np.pi * t) + noise

filtered_ecg = clean_ecg(raw_ecg)
print(f"Noise Variance Reduced: {np.var(raw_ecg) - np.var(filtered_ecg):.4f}")

plt.plot(raw_ecg)
# plt.plot(filtered_ecg)