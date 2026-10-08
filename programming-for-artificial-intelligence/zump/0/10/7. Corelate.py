import pandas as pd
from scipy import stats


df = pd.read_csv('student-mat.csv', sep=';')



# ---  Correlation Matrix ---
# Question: Which lifestyle factors are most negatively correlated with grades?
corr_matrix = df[['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G3']].corr()
g3_correlations = corr_matrix['G3'].sort_values()
print(g3_correlations)

