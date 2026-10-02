import numpy as np
import matplotlib.pyplot as plt

def bounded_2d_walk(steps, box_size=50):
    """
    Simulates a 2D random walk constrained within a box [-box_size, box_size].
    """
    # 1. Generate random steps for both X and Y axes
    # Steps are chosen from [-1, 0, 1] for both directions
    step_choices = np.array([-1, 0, 1])
    steps_x = np.random.choice(step_choices, size=steps)
    steps_y = np.random.choice(step_choices, size=steps)

    # 2. Calculate raw cumulative positions (Unbounded)
    path_x = np.cumsum(steps_x)
    path_y = np.cumsum(steps_y)

    # 3. Apply Boundaries (Reflective Logic)
    # If position > box_size, we push it back.
    # For simplicity in this example, we will 'clip' the values to the boundary.
    path_x = np.clip(path_x, -box_size, box_size)
    path_y = np.clip(path_y, -box_size, box_size)

    # Combine into a single (steps, 2) array
    return np.stack((path_x, path_y), axis=1)

# --- Calling the Simulation ---
n_steps = 1000
boundary = 20 # The walk stays within -20 and +20 on both axes
walk_data = bounded_2d_walk(n_steps, box_size=boundary)

# Final position check
print(f"Final Position: {walk_data[-1]}")
print(f"X-Bounds: Min {np.min(walk_data[:,0])}, Max {np.max(walk_data[:,0])}")
print(f"Y-Bounds: Min {np.min(walk_data[:,1])}, Max {np.max(walk_data[:,1])}")


plt.plot(walk_data)
plt.show();