import numpy as np

# --- 1. Beginner: Patient Risk Score (Dot Product) ---
def calculate_risk(vitals, weights):
    # vitals: [Age, BMI, BloodPressure]
    return np.dot(vitals, weights)

patient_a = np.array([[65, 30, 140], [45, 23, 125], [50, 13, 110]])
risk_weights = np.array([0.5, 0.2, 0.3])
score = calculate_risk(patient_a, risk_weights)
print(f"Patient Risk Score: {score}")



