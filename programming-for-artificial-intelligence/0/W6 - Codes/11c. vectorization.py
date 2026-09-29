#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:47:05 2026

@author: awais
"""

import numpy as np

# Feature Centering (Broadcasting) ---
def center_features(X):
    # X is (Samples, Features). Subtract mean of each column.
    return X - X.mean(axis=0)

X_train = np.random.rand(100, 5) # 100 patients, 5 features
centered_X = center_features(X_train)
print(f"Centered data (should be ~0): {centered_X}")
# print(f"Mean of centered data (should be ~0): {centered_X.mean(axis=0)}")
