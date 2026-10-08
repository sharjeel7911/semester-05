#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:01:54 2026

@author: awais
"""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# # MAP: Double every number
# doubled = list(map(lambda x: x * 2, nums))
# print("doubled after map", doubled)

# # FILTER: Only numbers > 3
# greater_than_three = list(filter(lambda x: x > 5, nums))
# print("filtered list", greater_than_three)

# REDUCE: Sum of all numbers
total = reduce(lambda x, y: x + y, nums)
print("reduced:", total)