import pandas as pd

# Assuming the file 'student-mat.csv' is in the directory
# Note: This dataset uses ';' as a separator
df = pd.read_csv('student-mat.csv', sep=';')

# Create a new column
df['total_grade'] = df['G1'] + df['G2'] + df['G3']

# Drop a column (axis=1 means column)
df_reduced = df.drop('total_grade', axis=1)
