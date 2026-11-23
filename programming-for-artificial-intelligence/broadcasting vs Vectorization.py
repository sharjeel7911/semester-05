# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:14:48 2026

@author: faiza.khadim
"""

# %%
#vectorization : is the process of applying an operation to
#all elements of an array at once, without explicitly writing a loop.
#output
import numpy as np
# Signal Gain ---
def apply_gain(signal, factor):
    return signal * factor

raw_signal = np.array([0.1, 0.2, 0.5, 0.1])
amplified = apply_gain(raw_signal, 10)
print(f"Amplified: {amplified}") 
# %%#vectorization b
import numpy as np

# Normalized Value
# {X-X_{min}}/X_{max}-X_{min}}

#(X-60)/(140-60)=(X-60)/(80)
# value	Calculation	              Normalized value
# 70	(70−60)/80	                 0.125
# 120	(120−60)/80	                 0.750
# 85	(85−60)/80	                 0.3125
# 140	(140−60)/80	                  1.000
# 60	(60−60)/80	                   0.000
# 110	(110−60)/80	                   0.625
# --- Normalization (ML Preprocessing) ---
def normalize_data(matrix):
    # Vectorized Min-Max Scaling
    return (matrix - matrix.min()) / (matrix.max() - matrix.min())
#patient heart rata, second column BP 
patient_vitals = np.array([
    [70, 120],
    [85, 140], 
    [60, 110]
 ])
norm_vitals = normalize_data(patient_vitals)
print(f"Normalized Vitals:\n{norm_vitals}")
# %%
#Broadcasting: 
#NumPy's ability to perform operations on arrays of different 
#but compatible shapes by automatically adjusting 
#how their elements are used.

# There are 3 main rules:
# 1. NumPy compares array dimensions from right to left.
# 2. Two dimensions are compatible if:
#    - They are equal, OR
#    - One of them is 1.
# 3. If the dimensions are not compatible, NumPy raises a ValueError

import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(a1+a2)
# %%
import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6,7,8])
print(a1+a2)
# %%
import numpy as np
a1=np.array([
              [1,2,3],
              [3,4,5]
            ])
a2=np.array([4])
print(a1+a2)

# %%
import numpy as np
a1=np.array([
              [1,2,3],
              [3,4,5]
              [7,8,9]
            ])
a2=np.array([
                [1,2],
                [3,4]
             ])
print(a1+a2)
# %%

import numpy as np
a1=np.array([
              [1,2],
              [2,3]
              [3,4]
            ])
a2=np.array([1,2,3])

print(a1+a2)
# %%
import numpy as np
a1=np.array([
              [1,2,3],
              [3,4,5]
            ])
a2=np.array([1,2,3])

print(a1+a2)
# %%3d
import numpy as np
a1=np.ones((2,3,5))
a2=np.ones((4,1,5))
print(a1)
print("*"*6)
print(a2)
#print(a1+a2)

# %%

import numpy as np
# --- Diagnostic Filter (Masking) ---
def find_anomalies(data, threshold):
    # Boolean Masking
    mask = data > threshold
    return data[mask]

heart_rates = np.array([72, 110, 65, 140, 80])
tachycardia = find_anomalies(heart_rates, 100)
print(f"Anomalous Heart Rates: {tachycardia}") # [110 140]

# %%
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

result = arr[(arr > 20) & (arr < 50)]

print(result)

# %%

arr = np.array([10, 20, 30, 40, 50])

result = arr[(arr < 20) | (arr > 40)]

print(result)
# %%

arr = np.array([10, 20, 30, 40, 50])

result = arr[~(arr > 30)]

print(result)

# %%
#Boolean masking is not limited to selecting elements. We can also modify them.

marks = np.array([30, 45, 60, 80, 40])

marks[marks < 50] += 10


print(marks)
# %%

marks = np.array([45, 70, 85, 30, 90])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)
# %%
#Both arrays must have the same number of dimensions
#All dimensions must be equal except the dimension along which we want to concatenate.
# axis=0: Rows are added (increased), while the number of columns remains the same.
# axis=1: Columns are added (increased), while the number of rows remains the same.
import numpy as np
a = np.array([
    [1, 2], 
    [3, 4]
   ])
b = np.array([
    [5, 6], 
    [7,8]
])

# Stack vertically (Result is 4x2)row
v_stack = np.concatenate((a, b), axis=0)
# Stack horizontally (Result is 2x4) col
h_stack = np.concatenate((a, b), axis=1)
print(v_stack)
print( h_stack)

# %%
#concatenate
import numpy as np

a = np.ones((2, 3, 4))
b = np.ones((2, 3, 5))

# axis=2
c = np.concatenate((a, b), axis=2)
print(c.shape)
# if axis=2: valid
# if axis=1: invalid
# if axis=0: invalid
# %%
import numpy as np
a = np.array([10, 20, 30, 40])
b = a[a > 20] #gemerate copy
b[0] = 999
print(a)
print(b)
# %%
#2d, 0,1,-1,-2
import numpy as np
matrix = np.array([
    [1, 2, 3, 4], 
    [4, 5, 6, 5], 
    [7, 8, 9, 6]
])
# Sum of EVERYTHING5S
print("Sum", np.sum(matrix)) # 60
print("Axis 0 Sum", np.sum(matrix, axis=0))#sum along columns(Vertical within layer)
print("Axis 1 Sum", np.sum(matrix, axis=1))#Sum along row (Horizontal within layer)
print("Axis -1 Sum", np.sum(matrix, axis=-1))
print("Axis -2 Sum", np.sum(matrix, axis=-2))
# axis=0	First dimension (colums)
# axis=1	Last dimension (rows)
# axis=-1	Last dimension (rows)
# axis=-2	First dimension (cols)
# For a 2D array:
# - axis=0 and axis=-2 refer to the same dimension(cols).
# - axis=1 and axis=-1 refer to the same dimension(rows).
# %%
#3d 0,1,2,-1,-2,-3
import numpy as np
arr = np.array([
    [
         [1, 2, 3],
         [4, 5, 6]
     ],

    [
     [7, 8, 9],
     [10, 11, 12]
     ]
])
print("Array:")
print(arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

print("Axis 0:", np.sum(arr, axis=0))#[1+7, 2+8, 3+9][14,16,18]each layer elements
print("Axis 1:", np.sum(arr, axis=1)) #cols
print("Axis 2:", np.sum(arr, axis=2))#

# print("Axis -1:", np.sum(arr, axis=-1))
# print("Axis -2:", np.sum(arr, axis=-2))
# print("Axis -3:", np.sum(arr, axis=-3))

# axis=0	axis=-3	Same result
# axis=1	axis=-2	Same result
# axis=2	axis=-1	Same result

# %%
#axis= 0,1,2,3,-1,-2,-3,-4
import numpy as np
a = np.arange(1, 49).reshape(2, 2, 3, 4)
print(a)
print(a.shape)

print(a[1][0])
