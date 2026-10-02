#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 01:18:37 2026

@author: awais
"""

def set_voltage(value, unit="Volts"):
    print(f"Setting: {value} {unit}")

set_voltage(220)          # Output: 220 Volts
set_voltage(5, "miliV")   # Output: 5 miliV