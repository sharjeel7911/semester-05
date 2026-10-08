#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:45:11 2026

@author: awais
"""

# Standard function
# def power(x, y): 
#     return y ** x
    
# print("Regular Function: ", add(5, 7))


# def indirectFunction(a, b, func_name):
#     val = func_name(a, b)
#     return val

# print("indirect call: ", indirectFunction(2, 5, power))


my_secret_func = lambda x, y : x ** y

p = my_secret_func(2, 6)
print(p)

# Lambda equivalent
# add_lambda = lambda x, y: x * y

# print("Lambda Function: ", indirectFunction(5, 7, add_lambda))
