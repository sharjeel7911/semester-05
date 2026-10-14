#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:54:12 2026

@author: awais
"""
# Closure: Datahiding /  encapsulation without using a class

def make_multiplier(n):
    
    def multiplier(x):
        return x * n    # x = 10, n = 3
    return multiplier

times3 = make_multiplier(3)

print(times3(10)) # 30 (Remembers that n was 3)

