import pandas as pd
import numpy as np

# Load dataset (using Math students as example)
df = pd.read_csv('student-mat.csv', sep=';')

# Question: Does more study time actually lead to higher final grades?
study_impact = df.groupby('studytime')['G3'].mean()
print(study_impact)

