#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:16:29 2026

@author: awais
"""
# Using range() (C++ Style)


matrix = [[1, 6, 2], [8, 3, 7], [4, 9, 5]]
results = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 5:
            results.append(matrix[i][j])
            
print ("Direct Translation using range(): ", results)