import pandas as pd

# Assuming the file 'student-mat.csv' is in the directory
# Note: This dataset uses ';' as a separator
df = pd.read_csv('student-mat.csv', sep=';')

# Inspection
print(df.head())      # First 5 rows
print(df.info())      # Column types and non-null counts
print(df.describe())  # Statistical summary of numerical columns
