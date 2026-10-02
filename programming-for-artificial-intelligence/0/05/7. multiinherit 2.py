#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:13:41 2026

@author: awais
"""

class A:
    def speak(self): print("A")
class B(A):
    def speak(self): print("B"); super().speak()
class C(A):
    def speak(self): print("C"); super().speak()
class D(B, C):
    def speak(self): super().speak()
    
d_obj = D()
d_obj.speak()
# Output:
# B
# C
# A
# Notice: 'A' is only called ONCE because of Python's C3 Linearization.