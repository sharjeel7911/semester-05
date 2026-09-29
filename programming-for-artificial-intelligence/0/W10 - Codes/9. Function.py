import pandas as pd


df = pd.read_csv('student-mat.csv', sep=';')

# --- Binning and Categorization ---
# Convert numeric grades into "Letter Grades"
def grade_to_letter(score):
    if score >= 15: return 'A'
    if score >= 10: return 'B'
    return 'F'

df['letter_grade'] = df['G3'].apply(grade_to_letter)

