import pandas as pd

# Assuming the file 'student-mat.csv' is in the directory
# Note: This dataset uses ';' as a separator
df = pd.read_csv('student-mat.csv', sep=';')

# iloc: Get the first 5 rows and first 3 columns by index
subset_idx = df.iloc[0:5, 0:3]

# loc: Get rows where G3 > 15, and only show 'school' and 'G3' columns
high_achievers = df.loc[df['G3'] > 15, ['school', 'G3']]
