# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:10:17 2026

@author: faiza.khadim
"""
import array # NUMERICAL VALUES
# 1. Integer array
a1 = array.array('i', [10, 20, 30])
# 2. Float array
a2 = array.array('f', [10.5, 20.5, 30.5])
# 3. Double precision float
a3 = array.array('d', [10.5, 20.5, 30.5])
# 4. Signed character (integer byte)POSITIVE, NEGATIVE,
#B dont store negative
a4 = array.array('b', [10, 20, -30])
# 5. Unsigned integer(only positive)
a5 = array.array('I', [10, 20, 30])
a33 = array.array('u', ['A', 'B', 'C'])
aa = array.array('u', 'FAIZA')
# Display arrays
print(a1.tolist())
print(a2.tolist())
print(a3.tolist())
print(*a4)
print(*a33)
print(*aa)
# %%
import numpy as np
a1 = np.array([10, 20, 30], dtype='i')
a2 = np.array([10.5, 20.5, 30.5], dtype='f')
a3 = np.array([10.5, 20.5, 30.5], dtype='d')
a4 = np.array([True, False, True], dtype='bool')
a5 = np.array(["Ali", "Sara", "Ahmed"], dtype='str')

print(a1, a1.dtype)
print(a2, a2.dtype)
print(a3, a3.dtype)
print(a4, a4.dtype)
print(a5,a5.dtype )
# %%
x = 3
m1 = []
for i in range(x):          # Outer loop
    row = []
    for j in range(x):      # Inner loop
        row.append(j)
    m1.append(row)
print(m1)
# %%
import time
x=10000
#matrix = [[expression for j in range(columns)] for i in range(rows)]
m1=[ [j for j in range(x)]
        for i in range(x)]

m2=[ [j for j in range(x)]
     for i in range(x)]

start=time.time()
for i in range(x):
    for j in range(x):
        m1[i][j]+=m2[i][j]
        
end=time.time()
print(f"{end-start:.6f} sec")
# %%
import numpy as np
x=10000
m1=[ [j for j in range(x)]
    for i in range(x)]
m2=[ [j for j in range(x)]
     for i in range(x)]
a1=np.array(m1)
a2=np.array(m2)

start=time.time()
m1+m2
end=time.time()
print(f"{end-start:.6f} sec")
# %%
marks = [70, 80, 90, 60]
updated_marks = []
for mark in marks:
    updated_marks.append(mark + 5)
print(updated_marks)
# %%
#vectorization
import numpy as np
marks = np.array([70, 80, 90, 60])
updated_marks = marks + 5
print(updated_marks)
#NumPy automatically performed the operation on every element.
# %%
#Broadcasting: NumPy automatically uses a smaller array with a bigger array to perform an operation.
A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
B = np.array([1, 2, 3])
print(A + B)
# %%
import numpy as np
#2d array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix.ndim)
print(matrix.shape)
print(matrix)
print("*"*70)

# %%
#2 sections,each section contain 3 students, 
#each student has 4 subject marks
import numpy as np
marks = np.array([
    [
        [80, 75, 90, 85],
        [70, 85, 88, 78],
        [90, 92, 95, 89]
    ],
    [
        [65, 78, 82, 80],
        [90, 92, 95, 88],
        [75, 80, 85, 90]
    ]
])

print(marks)
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)

print(marks[0])
# print(marks[1])
print(marks[1][0][3])

# %%
#using list
a = [10, 20, 30, 40]
b = a
b[0] = 99
print("List a:", a)
print("List b:", b)
# %%
a = [10, 20, 30, 40]
b = a.copy()
b[0] = 99
print("Original List a:", a)
print("New List b:", b)
# %%
import numpy as np
x = np.array([10, 20, 30, 40, 50])
y = x[1:4]
y[0] = 99
print(x)
print("\n",y)

# %%
import numpy as np
x = np.array([10, 20, 30, 40, 50])
y = x[1:4].copy()
y[0] = 99
print(x)
print(y)
# %%
#built in function
import numpy as np
#ND Array (3D Exampe: 2 layers, 3 rows, 2 columns)
#a33= np.zeros((2, 3, 2)) 
#a2 = np.ones((2,2))
#a3 = 10* np.ones((2,2)) 
#a4 = np.full((2,2), 11) #any value
#a5 = np.empty((2,2))
a1 = np.arange(0, 10, 2) #start, end, step
a22 = np.linspace(0, 1, 100)#(start, stop, num)
print(a22)
# %%
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
x = a + b
print(x)
# %%
a = np.array([[2, 4, 6],
              [1, 3, 5]])
b = np.array([1, 2, 3])
print(a * b)
# %%
#special cases, R1
x1 = np.arange(0, 5, 0.5, dtype=int)
x2 = np.arange(-3, 3, 0.5, dtype=int)
print(x1,x2)
# %%
import numpy as np
data = np.array([
    [10, 2], 
    [20, 5],
    [30, 8]
])
x = np.sum(data, axis=1) # if 0 column , otherwise row wise
print(x)
# %%
# A 2D Matrix (3 rows, 2 columns)
data = np.array([
    [10, 20], 
    [30, 40], 
    [50, 60]
])
print(f"Shape: {data.shape}") # (3, 2)
print(f"Size:  {data.size}")  # 6
print(f"Dims:  {data.ndim}")  # 2
print(f"Type:  {data.dtype}") # int64 (on most systems)
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
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise Math
print(a + b)  # [5, 7, 9]
print(a * b)  # [4, 10, 18]
# Scalar Operations
print(a+5)
print(a ** 2) # [1, 4, 9] (Square each element)

b = np.append(b, 10)
try:
     print(a + b)
except Exception as e:
     print (e)
    
# %%
#reshape array
import numpy as np
raw_data = np.arange(12) # [0, 1, 2... 11]
print(raw_data)

# Reshape to 3 rows, 4 columns
grid = raw_data.reshape(3, 4)
print(grid)

# Reshape to 3D (2 layers, 3 rows, 2 columns)
cube = raw_data.reshape(2, 3, 2)
print(cube)

auto_grid = raw_data.reshape(2, -1) #totalelemnts/rows
print(auto_grid)
# Flatten: Back to 1D
flat = grid.ravel()
print(flat)
# %%
#transpose
import numpy as np
# Swap rows and columns, # original.shape is (2, 4)
original = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8]
])
print(original)
transposed = original.T 
print(transposed)
# transposed.shape is (4, 2)
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
# axis=0	First dimension (rows)
# axis=1	Last dimension (columns)
# axis=-1	Last dimension (columns)
# axis=-2	First dimension (rows)
# For a 2D array:
# - axis=0 and axis=-2 refer to the same dimension.
# - axis=1 and axis=-1 refer to the same dimension.
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
print("Axis 1:", np.sum(arr, axis=1)) #sum along columns (Vertical within layer)
print("Axis 2:", np.sum(arr, axis=2))#Sum along rows (Horizontal)

# print("Axis -1:", np.sum(arr, axis=-1))
# print("Axis -2:", np.sum(arr, axis=-2))
# print("Axis -3:", np.sum(arr, axis=-3))

# axis=0	axis=-3	Same result
# axis=1	axis=-2	Same result
# axis=2	axis=-1	Same result
# %%
#append
import numpy as np
base = np.array([1, 2, 3])
# Adding a single value
new_arr = np.append(base, [4, 5])
print(new_arr)
# %%
#Both arrays must have the same number of dimensions(1d,2d)
#All dimensions must be equal except the dimension along which we want to concatenate.
import numpy as np
a = np.array([
    [1, 2], 
    [3, 4]
   ])
b = np.array([
    [5, 6], 
    [7,8]
])

# Stack vertically (Result is 4x2)
v_stack = np.concatenate((a, b), axis=0)
# Stack horizontally (Result is 2x4)
h_stack = np.concatenate((a, b), axis=1)
print(v_stack)
print( h_stack)
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
#output, Broadcasting
import numpy as np

def center_features(X):
    return X - X.mean(axis=0) #column wise
X = np.array([
    [10, 20, 30],
    [20, 30, 40],
    [30, 40, 50]
])
centered_X = center_features(X)
print("Original Data:")
print(X)
print("\nCentered Data:")
print(centered_X)
#print(centered_X.dtype)

print("\nColumn Means:")
print(centered_X.mean(axis=0))

# %%
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr > 25)       
print(arr[arr > 25])

# %%

import numpy as np
# --- Windowing ---
def get_window(signal, start, end):
    return signal[start:end]

data = np.arange(0, 100, 1) # Dummy signal
segment = get_window(data, 10, 20)
print(f"Data Segment: {segment}")
# %%
#visualization library.
#pyplot: module name
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("My First Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
# %%
import numpy as np
import matplotlib.pyplot as plt

students = np.array(["Ali", "Sara", "Ahmed", "Ayesha"])
marks = np.array([70, 85, 60, 95])

plt.bar(students, marks)
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
# %%
import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5, 6])
marks = np.array([35, 40, 55, 65, 80, 90])
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()
plt.show()
# %%

import numpy as np
import matplotlib.pyplot as plt

data = np.array([10, 20, 30, 40, 50])

centered = data - np.mean(data)

plt.plot(data, label="Original Data")
plt.plot(centered, label="Centered Data")

plt.title("Feature Centering")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()
# %%

import numpy as np
import matplotlib.pyplot as plt

# 1. Generate random marks for 20 students
marks = np.random.randint(0, 101, 20)

# 2. Calculate average marks
average = np.mean(marks)

# 3. Print marks
print("Student Marks:", marks)
print("Average Marks:", average)

# 4. Create Histogram
plt.hist(marks, bins=10, edgecolor='black')

# 5. Add average line
plt.axvline(average, label="Average Marks")

# 6. Graph labels
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.legend()
plt.grid(axis='y')#show only horizontl line

# 7. Display graph
plt.show()
# %%
import numpy as np
# --- Log-Transformation (Image Processing) ---
def log_transform(image_pixels):
    # Common in X-ray enhancement to expand dark pixels
    return np.log1p(image_pixels)  #natural log:log(1+x)

xray_patch = np.array([10, 50, 100, 255])
enhanced = log_transform(xray_patch)
print(f"Log Enhanced: {enhanced}")
# %%

import numpy as np

# --- Cumulative Dosage ---
def track_dosage(hourly_intake):
    # Using ufunc accumulate
    return np.add.accumulate(hourly_intake)

doses = np.array([5, 0, 10, 5]) # mg per hour
total_in_system = track_dosage(doses)
print(f"Cumulative Dose: {total_in_system}") # [5 5 15 20]

# %%
# Task: Generate 50 random students' marks using NumPy and visualize their distribution using Matplotlib.

# Requirements:
# 1. Generate 50 random marks between 0 and 100.
# 2. Calculate average using np.mean().
# 3. Display marks using plt.hist().
# 4. Add a vertical average line using plt.axvline().
# 5. Add title, labels and legend.
# marks = np.random.randint(0, 101, 50)#start,end,size
# average = np.mean(marks)

i