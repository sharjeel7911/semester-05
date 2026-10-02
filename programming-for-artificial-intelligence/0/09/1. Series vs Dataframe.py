import pandas as pd

# 1. Create a Series (A single column)
grades = pd.Series([15, 12, 18, 10], name="G3")

# 2. Create a DataFrame (The whole table)
data = {
    'Name': ['Ali', 'Sara', 'Zain', 'Hina'],
    'G3': [15, 12, 18, 10],
    'Absences': [2, 5, 0, 8]
}
df = pd.DataFrame(data)

print(df)
