#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:54:57 2026

@author: awais
"""

import numpy as np

# --- Cumulative Dosage ---
def track_dosage(hourly_intake):
    # Using ufunc accumulate
    return np.add.accumulate(hourly_intake)

doses = np.array([5, 0, 10, 5]) # mg per hour
total_in_system = track_dosage(doses)
print(f"Cumulative Dose: {total_in_system}") # [5 5 15 20]