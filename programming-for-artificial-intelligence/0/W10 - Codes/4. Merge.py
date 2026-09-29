import pandas as pd
import numpy as np

# Load dataset (using Math students as example)
df = pd.read_csv('student-mat.csv', sep=';')


# Scenario: Some students are in both Math and Por classes.
df_mat = pd.read_csv('student-mat.csv', sep=';')
df_por = pd.read_csv('student-por.csv', sep=';')

# We merge on common demographic columns to find "dual-subject" students
common_cols = ["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"]
combined_df = pd.merge(df_mat, df_por, on=common_cols, suffixes=('_mat', '_por'))
print(f"Students enrolled in both subjects: {combined_df.shape[0]}")s
