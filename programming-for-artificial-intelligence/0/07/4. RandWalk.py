import numpy as np
import matplotlib.pyplot as plt

def simulate_hr_walk(start_hr, steps, step_size=1):
    # Generate random steps: -1 or +1
    random_steps = np.random.choice([-step_size, step_size], size=steps)

    # Cumulative sum turns steps into a path
    # Path = start + cumulative sum of all previous steps
    path = start_hr + np.cumsum(random_steps)
    return path

# --- Calling ---
initial_hr = 70
total_minutes = 600 # 10 hours of monitoring
hr_trend = simulate_hr_walk(initial_hr, total_minutes)

print(f"Final HR after 10 hours: {hr_trend[-1]}")
print(f"Max HR reached: {np.max(hr_trend)}")

plt.plot(hr_trend)
plt.show()
