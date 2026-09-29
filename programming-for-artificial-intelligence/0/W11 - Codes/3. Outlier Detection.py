# Identify "Outlier" students (extremely high/low absences) and see how they skew the correlation.

# Z-Score Outlier Detection and Impact on Correlation

# 1. Calculate Z-Scores for Absences
df['abs_z'] = np.abs(stats.zscore(df['absences']))

# 2. Identify Outliers (Z > 3 means the point is 3+ std devs away)
outliers = df[df['abs_z'] > 3]
clean_df = df[df['abs_z'] <= 3]

# 3. Compare Correlation between Absences and G3 before and after
raw_corr = df['absences'].corr(df['G3'])
clean_corr = clean_df['absences'].corr(clean_df['G3'])

print(f"Number of outliers detected: {len(outliers)}")
print(f"Correlation (With Outliers): {raw_corr:.4f}")
print(f"Correlation (Without Outliers): {clean_corr:.4f}")

# Visualize the outlier impact
plt.scatter(df['absences'], df['G3'], color='blue', label='Normal')
plt.scatter(outliers['absences'], outliers['G3'], color='red', label='Outliers')
plt.legend()
plt.show()
