import pandas as pd
from scipy import stats


df = pd.read_csv('student-mat.csv', sep=';')


# --- Descriptive Stats ---
stats_summary = df[['absences', 'G3']].describe()

