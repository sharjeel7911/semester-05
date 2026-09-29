import pandas as pd

# Assuming the file 'student-mat.csv' is in the directory
# Note: This dataset uses ';' as a separator
df = pd.read_csv('student-mat.csv', sep=';')

# Select a single column (returns a Series)
absences = df['absences']

# Select multiple columns (returns a DataFrame)
grades = df[['G1', 'G2', 'G3']]
