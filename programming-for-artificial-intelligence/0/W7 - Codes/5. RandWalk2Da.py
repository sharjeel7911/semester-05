#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:15:07 2026

@author: awais
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation Code (from previous answer) ---
def bounded_2d_walk(steps, box_size=50):
    np.random.seed(16) # Fixed seed for reproducible output
    step_choices = np.array([-1, 0, 1])
    steps_x = np.random.choice(step_choices, size=steps)
    steps_y = np.random.choice(step_choices, size=steps)
    
    # Cumulative sum turns steps into a path
    path_x = np.cumsum(steps_x)
    path_y = np.cumsum(steps_y)
    
    # --- The Bounding Logic (Clipped) ---
    path_x = np.clip(path_x, -box_size, box_size)
    path_y = np.clip(path_y, -box_size, box_size)
    
    # Combine into (steps, 2) array
    return np.stack((path_x, path_y), axis=1)

# --- 2. Generate the Walk Data ---
n_steps = 1000
boundary = 30 # The walk stays within -30 and +30 on both axes
walk_data = bounded_2d_walk(n_steps, box_size=boundary)

# Final position check
print(f"Final Position: {walk_data[-1]}")
print(f"X-Bounds: Min {np.min(walk_data[:,0])}, Max {np.max(walk_data[:,0])}")
print(f"Y-Bounds: Min {np.min(walk_data[:,1])}, Max {np.max(walk_data[:,1])}")


# --- 3. Matplotlib Plotting ---
plt.figure(figsize=(10, 8))

# A. Plot the complete path (X values are in col 0, Y values in col 1)
plt.plot(walk_data[:,0], walk_data[:,1], label='Random Path', alpha=0.6, linewidth=1, color='blue')

# B. Mark the START point (index 0)
plt.scatter(walk_data[0,0], walk_data[0,1], color='green', marker='o', s=100, label='Start (Origin)')

# C. Mark the END point (index -1)
plt.scatter(walk_data[-1,0], walk_data[-1,1], color='red', marker='X', s=150, label='Final Position')

# D. Setup Axes and Boundaries
# Crucial: Must set xlim and ylim to see the boundaries clearly
padding = 5
limit = boundary + padding
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)

# Draw the actual boundary box for visualization
plt.axhline(boundary, color='black', linestyle='--', alpha=0.5)
plt.axhline(-boundary, color='black', linestyle='--', alpha=0.5)
plt.axvline(boundary, color='black', linestyle='--', alpha=0.5)
plt.axvline(-boundary, color='black', linestyle='--', alpha=0.5)

# Formatting
plt.title(f"2D Bounded Random Walk Simulation ({n_steps} Steps)")
plt.xlabel("X Position (Microns or Arbitrary Units)")
plt.ylabel("Y Position")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Equal aspect ratio ensures a circle looks like a circle, or a square like a square
plt.gca().set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()