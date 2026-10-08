#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:51:56 2026

@author: awais
"""

def special_func(a):
    print(f"calling special_func for {a}")
    return 2**a

nums = [1, 23, 55, 100, -5, 1.24]
# new_nums = []
# for i in nums:
#     new_nums.append(i * 2)
    
# print(new_nums)

# new_nums = [x*2 for x in nums]
# print (new_nums)

new_nums = [special_func(x) for x in nums]
print(new_nums)




# List Comprehension: Square of even numbers
# squares = [x**2 for x in range(3,10,2)]
# print(squares)

# Dictionary Comprehension: Mapping names to lengths
# names = ["Ali", "Ahmed", "Sara", "Arsalan"]
# name_len = {n: len(n) for n in names}
# print(name_len)

