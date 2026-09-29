import pandas as pd


df = pd.read_csv('student-mat.csv', sep=';')


# --- Lambda Functions ---
# Create a "High Risk" flag for students with high alcohol consumption AND high failures
df['high_risk'] = df.apply(lambda row: 1 if row['Dalc'] > 3 and row['failures'] > 0 else 0, axis=1)
