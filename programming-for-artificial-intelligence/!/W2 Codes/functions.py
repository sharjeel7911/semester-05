# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:10:52 2026

@author: Awais
"""

def my_sepcial_func(a, b=-5, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    return "Awais", 23, "P4AI"
    
    
name, location, _ = my_sepcial_func(5, c= 55, d = 18, e = 57)    
