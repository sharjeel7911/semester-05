#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:58:09 2026

@author: awais
"""
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.4f}s")
        return result
    return wrapper

@timer_decorator
def slow_math(a, b):
    print("called")
    time.sleep(1)
    return "Done :" + str(a - b)

# slow_math = timer_decorator(slow_math)

print(slow_math(b = 5, a = 9))

