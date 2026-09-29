#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:50:27 2026

@author: awais
"""
import numpy as np
import matplotlib.pyplot as plt


# Synthetic Pulse Wave ---
def generate_pulse(timesteps):
    return np.sin(timesteps)

time = np.linspace(0, 2 * np.pi, 5)
pulse = generate_pulse(time)
print(f"Pulse Wave: {pulse}")

plt.plot(pulse)
