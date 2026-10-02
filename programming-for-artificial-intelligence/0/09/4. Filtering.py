import pandas as pd

# Assuming the file 'student-mat.csv' is in the directory
# Note: This dataset uses ';' as a separator
df = pd.read_csv('student-mat.csv', sep=';')

# Filtering students from Urban areas with more than 10 absences
urban_high_absence = df[(df['address'] == 'U') & (df['absences'] > 10)]

print(f"Count: {len(urban_high_absence)}")
