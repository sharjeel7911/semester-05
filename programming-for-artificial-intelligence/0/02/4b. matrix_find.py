#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:21:29 2026

@author: awais
"""
# Direct Iteration without using range

matrix = [[1, 6, 2], [8, 3, 7], [4, 9, 5]]

results = []
for row in matrix:
    for item in row:
        if item > 5:
            results.append(item)
            
print ("Direct Iteration: ", results)