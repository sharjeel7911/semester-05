import numpy as np

# --- 2. Intermediate: Solving for Dosage (Systems of Equations) ---
def solve_dosage(coefficients, targets):
    # Ax = b -> solve for x
    return np.linalg.solve(coefficients, targets)

# 2 drugs (x, y) with different effects on 2 symptoms
# 2x + 1y = 10 (Symptom A target)
# 1x + 3y = 15 (Symptom B target)
A = np.array([[2, 1], [1, 3]])
b = np.array([10, 15])
optimal_dosage = solve_dosage(A, b)
print(f"Optimal Drug X and Y dosages: {optimal_dosage}")
