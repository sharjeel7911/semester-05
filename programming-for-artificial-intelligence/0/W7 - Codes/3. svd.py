import numpy as np

# --- 3. Advanced: SVD for Data Compression (PCA-style) ---
def compress_signal(data_matrix):
    # Singular Value Decomposition
    U, S, Vt = np.linalg.svd(data_matrix)
    return U, S, Vt

# 500 samples of 12-lead ECG data
ecg_matrix = np.random.randn(500, 12)
U, S, Vt = compress_signal(ecg_matrix)
print(f"Top 3 singular values (Importance): {S[:3]}")
