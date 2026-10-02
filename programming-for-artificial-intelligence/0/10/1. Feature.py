import pandas as pd
df = pd.read_csv('student-mat.csv', sep=';')

# Calculate if a student improved from 1st to 2nd period
df['improvement'] = df['G2'] - df['G1']

# Filter for students who improved by more than 2 points
star_students = df[df['improvement'] >= 2]
