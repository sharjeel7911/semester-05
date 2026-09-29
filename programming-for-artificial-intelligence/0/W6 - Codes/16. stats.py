#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 04:20:15 2026

@author: awais
"""

from scipy import stats

def compare_models(acc_model_a, acc_model_b):
    # Perform an Independent T-test
    t_stat, p_value = stats.ttest_ind(acc_model_a, acc_model_b)
    return p_value

# --- Calling ---
# Accuracy results from 5 different test folds
model_a = [0.85, 0.88, 0.84, 0.86, 0.87, 0.75]
model_b = [0.91, 0.92, 0.90, 0.93, 0.91, 0.88]

p = compare_models(model_a, model_b)
print(f"P-value: {p:.5f}") 
# If p < 0.05, the difference is "Statistically Significant"