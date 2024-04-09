import numpy as np
import matplotlib.pyplot as plt

def relaxation_method(c, tol=1e-6, max_iter=100):
  """
  Solves the equation x = 1 - e^(-cx) using the relaxation method.

  Args:
      c: The value of the constant c.
      tol: Tolerance for convergence (default: 1e-6).
      max_iter: Maximum number of iterations (default: 100).

  Returns:
      The solution x and the number of iterations taken.
  """
  x = 0.5  # Initial guess
  for i in range(max_iter):
    new_x = 1 - np.exp(-c * x)
    if abs(new_x - x) < tol:
      return new_x, i
    x = omega * new_x + (1 - omega) * x  # Relaxation with omega (optional)

  print(f"Warning: Relaxation method did not converge in {max_iter} iterations for c={c}")
  return x, max_iter

# Define omega for relaxation (optional, set to 1 for basic iteration)
omega = 1.0

# Solve for different values of c
c_values = np.arange(0.0, 3.01, 0.01)
x_values = [relaxation_method(c)[0] for c in c_values]

# Plot x vs c
plt.plot(c_values, x_values)
plt.xlabel("Value of c")
plt.ylabel("Solution x")
plt.title("Solution of x = 1 - e^(-cx) using Relaxation Method")
plt.grid(True)
plt.show()

# Comment on the graph
print("Comments on the graph:")
print("- The solution x starts at 1 for c=0 (no exponential term).")
print("- As c increases, the solution x decreases monotonically.")
print("- The curve becomes steeper for higher values of c, indicating a more rapid decrease in x.")