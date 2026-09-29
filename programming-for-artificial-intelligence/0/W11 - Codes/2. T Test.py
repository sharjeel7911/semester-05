# Do students in Urban areas ($address='U'$) perform better than Rural areas ($address='R'$) significantly?

# Independent T-Test
urban_grades = df[df['address'] == 'U']['G3']
rural_grades = df[df['address'] == 'R']['G3']

# Perform T-test
t_stat, p_value = stats.ttest_ind(urban_grades, rural_grades)

print(f"Urban Mean: {urban_grades.mean():.2f}")
print(f"Rural Mean: {rural_grades.mean():.2f}")
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: Significant difference found between Urban and Rural performance.")
else:
    print("Conclusion: No significant difference found.")
