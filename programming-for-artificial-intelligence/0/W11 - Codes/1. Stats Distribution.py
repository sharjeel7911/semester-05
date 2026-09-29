# Understand the spread of final grades ($G3$).

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('student-mat.csv', sep=';')

# Basic Stats and Normality Check
mean_g3 = df['G3'].mean()
std_g3 = df['G3'].std()

# Check if G3 follows a Normal Distribution using Shapiro-Wilk test
# H0: Data is normal. If p > 0.05, it is normal.
stat, p_val = stats.shapiro(df['G3'])

print(f"Mean Grade: {mean_g3:.2f}, Std Dev: {std_g3:.2f}")
print(f"Shapiro-Wilk P-value: {p_val:.4f} (Is it Normal? {p_val > 0.05})")
