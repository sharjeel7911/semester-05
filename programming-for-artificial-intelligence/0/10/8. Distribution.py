import pandas as pd
from scipy import stats


df = pd.read_csv('student-mat.csv', sep=';')



# --- Probability Distributions (Z-Score) ---
# Question: Which students are "Outliers" (scoring way above/below the mean)?
df['z_score'] = np.abs(stats.zscore(df['G3']))
outliers = df[df['z_score'] > 2] # Students more than 2 std devs away
