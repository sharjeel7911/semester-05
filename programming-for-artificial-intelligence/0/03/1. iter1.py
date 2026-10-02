#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:42:12 2026

@author: awais
"""

# iterator class defnes next() function

nums = [10, 20, 30, 70]
it = iter(nums)         # returns an iterator for the list nume

print(next(it)) # 10
print(next(it)) # 20
print(next(it)) # 30
print(next(it)) # 30

print(next(it)) # Raises StopIteration