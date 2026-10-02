#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 04:09:48 2026

@author: awais
"""

import numpy as np

# Coefficients are [1, -3, 2] for 1*x**2 + -3*x**1 + 2*x**0
coefficients = [1, -3, 2, -5, 0]

# Use numpy.roots to find the roots
roots = np.roots(coefficients)

print("The roots of the polynomial are:", roots)