import pandas as pd
import numpy as np

# Load dataset (using Math students as example)
df = pd.read_csv('student-mat.csv', sep=';')

# Question: How do Gender and Address (Urban vs Rural) affect absences?
pivot_absences = df.pivot_table(values='absences', index='sex', columns='address', aggfunc='mean')
print(pivot_absences)

