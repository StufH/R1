import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# --- 1. Input Data ---
# Provided data points (ignoring the "run" labels)
vinkel = np.array([0, 5, 15, 25, 30, 40, 60]) # Angle in degrees
akselerasjon = np.array([0, 0.804, 2.46, 4.02, 4.7, 6.06, 8.08]) # Acceleration

# Convert angles from degrees to radians, as numpy's sin function expects radians
vinkel_rad = np.radians(vinkel)

# --- 2. Define the Sine Function Model ---
# Same model as before: A * sin(B*x + C) + D
def sine_function(x, A, B, C, D):
  """
  Defines a sine wave model.
  A * sin(B*x + C) + D
  x is expected to be in radians here.
  """
  return A * np.sin(B * x + C) + D

# --- 3. Perform the Regression (Curve Fitting) ---

# Provide initial guesses for the parameters [A, B, C, D].
# Estimating from the data:
# A (Amplitude): Max value is ~8. Let's guess something slightly larger, maybe 9 or 10 (potentially related to g*sin(theta)).
# B (Frequency Factor): If it's like sin(theta), B should be 1. Let's start with 1.
# C (Phase Shift): Starts near (0,0), so guess 0.
# D (Vertical Offset): Starts near (0,0), so guess 0.
initial_guesses = [9.0, 1.0, 0.0, 0.0]

# Use curve_fit to find the best parameters
# We use vinkel_rad (radians) as the x_data for the sine function
try:
    optimal_params, covariance = curve_fit(
        sine_function,
        vinkel_rad,      # Use radians for the fit function
        akselerasjon,
        p0=initial_guesses, # Pass the initial guesses
        maxfev=5000        # Increase max function evaluations if needed
    )
    print("Optimal parameters found:")
    print(f"  Amplitude (A): {optimal_params[0]:.4f}")
    print(f"  Frequency Factor (B): {optimal_params[1]:.4f}")
    print(f"  Phase Shift (C): {optimal_params[2]:.4f} (radians)")
    print(f"  Vertical Offset (D): {optimal_params[3]:.4f}")

    # Generate y values using the fitted model for plotting
    # Create a smooth range of angles (in radians) for plotting the curve
    vinkel_rad_smooth = np.linspace(vinkel_rad.min(), vinkel_rad.max(), 200)
    y_fitted = sine_function(vinkel_rad_smooth, *optimal_params) # Use '*' to unpack parameters

except RuntimeError:
    print("Error - curve_fit failed to converge. Try different initial guesses or check data.")
    optimal_params = None
    y_fitted = None
except ValueError as e:
    print(f"Error during curve fitting: {e}")
    print("Check data shapes and initial parameters.")
    optimal_params = None
    y_fitted = None


# --- 4. Plot the Results ---
plt.figure(figsize=(10, 6))

# Plot the original data points (using degrees for the x-axis is more intuitive here)
plt.scatter(vinkel, akselerasjon, label='Målte data punkter', color='blue', zorder=5) # zorder puts points on top

# Plot the fitted sine wave if the fit was successful
if y_fitted is not None:
    # Convert the smooth radian angles back to degrees for the plot axis
    vinkel_deg_smooth = np.degrees(vinkel_rad_smooth)
    plt.plot(vinkel_deg_smooth, y_fitted, label='Tilpasset sinusbølge', color='red', linewidth=2)

# Add labels and title (using Norwegian terms based on input)
plt.title('Sinusoidal regresjonsmodell for Vinkel vs. Akselerasjon')
plt.xlabel('Vinkel (grader)')
plt.ylabel('Akselerasjon')
plt.legend()
plt.grid(True)
plt.show()

# --- Optional: Check if it resembles g*sin(theta) ---
if optimal_params is not None:
    print("\nComparison with g*sin(theta):")
    print(f"The fitted amplitude A ({optimal_params[0]:.2f}) might represent 'g'.")
    # Standard gravity g is approx 9.81 m/s^2
    print(f"The fitted frequency factor B ({optimal_params[1]:.2f}) is close to 1, as expected for sin(theta).")
    print(f"The fitted phase shift C ({optimal_params[2]:.2f} rad) is close to 0, as expected.")
    print(f"The fitted vertical offset D ({optimal_params[3]:.2f}) is close to 0, as expected.")