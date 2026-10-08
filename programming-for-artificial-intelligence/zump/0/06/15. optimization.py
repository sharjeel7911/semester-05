#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:28:06 2026

@author: awais
"""
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def objective_function(x):
    # f(x) = (x-3)^2 + 5. We want to find the x that minimizes this.
    return (x - 3)**2 + 5*x - 7

# --- Calling ---
initial_guess = [0]
result = minimize(objective_function, initial_guess)

print(f"Optimal x: {result.x[0]:.2f}") # Output: ~3.00
print(f"Minimum value: {result.fun:.2f}") # Output: 5.00


# Create x values and calculate y = x^2
x = np.linspace(-10, 10, 2000)  # Generate 100 points
y = objective_function(x)

# Plot the function, add labels/title, and display
# plt.plot(x, y, label='y=x^2')
# plt.title("Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend() # Show the label
plt.show()