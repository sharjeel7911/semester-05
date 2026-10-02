import pandas as pd
# df = pd.read_csv('student-mat.csv', sep=';')


# Create a dummy series with missing data for demonstration
s = pd.Series([10, np.nan, 12, np.nan, 15])

# --- EASY: Detecting and Dropping ---
print(s.isna().sum()) # Count missing
clean_s = s.dropna()  # Remove them

# --- MEDIUM: Filling with Mean/Median ---
# Filling missing grades with the average of the class
df['G3'] = df['G3'].fillna(df['G3'].mean())

# --- COMPLEX: Forward/Backward Fill (Time Series Style) ---
# Useful if data is ordered; assumes the next value is similar to the last
df_filled = df.ffill()
