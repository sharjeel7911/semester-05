#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:09:19 2026

@author: awais
"""
import numpy as np

a1 = np.arange(0, 10, 2)


a2 = np.linspace(0, 1, 100)


#special cases

x1 = np.arange(0, 5, 0.5, dtype=int)

x2 = np.arange(-3, 3, 0.5, dtype=int)

power = 40
modulo = 10000
x3 = [(n ** power) % modulo for n in range(8)]
x4 = [(n ** power) % modulo for n in np.arange(8)]
