import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def P(x):
  return 924 * x**6 - 2772 * x**5 + 3150 * x**4 - 1680 * x**3 + 420 * x**2 - 42 * x + 1

# Define the derivative of the polynomial
def P_prime(x):
  return 5544 * x**5 - 13860 * x**4 + 12600 * x**3 - 5040 * x**2 + 840 * x - 42

# Plotting function (same as before)
def plot_P(x):
  x = np.linspace(0, 1, 1000)
  plt.plot(x, P(x))
  plt.xlabel("x")
  plt.ylabel("P(x)")
  plt.title("Plot of P(x) = 924x^6 - 2772x^5 + ... + 1")
  plt.grid(True)
  plt.show()

# Newton's method function (same as before)
def newton_method(f, df, x0, tol=1e-10, max_iter=100):
  for i in range(max_iter):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol:
      return x1
    x0 = x1
  print(f"Warning: Newton's method did not converge in {max_iter} iterations for x0={x0}")
  return None

# Secant method function
def secant_method(f, x0, x1, tol=1e-10, max_iter=100):
  """
  Finds a root of f(x) = 0 using the secant method with initial guesses x0 and x1.

  Args:
      f: The function to solve.
      x0, x1: Initial guesses for the root.
      tol: Tolerance for convergence (default: 1e-10).
      max_iter: Maximum number of iterations (default: 100).

  Returns:
      The approximate root or None if not found within tolerance and iterations.
  """
  for i in range(max_iter):
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    if abs(x2 - x1) < tol:
      return x2
    x0 = x1
    x1 = x2
  print(f"Warning: Secant method did not converge in {max_iter} iterations for x0={x0}, x1={x1}")
  return None

# Plot P(x) (uncomment to plot)
# plot_P(x)

# Initial guesses for roots (adjust as needed)
x0_guesses_newton = [0.2, 0.4, 0.6, 0.8]  # Modify for Newton's method
x0_secant = 0.1  # Initial guess for x0 in secant method (adjust based on plot)
x1_secant = 0.3  # Initial guess for x1 in secant method (adjust based on plot)

# Find roots using Newton's method
roots_newton = [newton_method(P, P_prime, x0, tol=1e-10) for x0 in x0_guesses_newton if newton_method(P, P_prime, x0)]

# Find a root using the secant method
root_secant = secant_method(P, x0_secant, x1_secant, tol=1e-10)

if roots_newton:
  print("Roots of P(x) = 0 found using Newton's method (at least 10 decimal places):")
  for root in roots_newton:
    print(f"{root:.10f}")

if root_secant:
  print(f"\nRoot of P(x) = 0 found using the secant method (at least 10 decimal places):")
  print(f"{root_secant:.10f}")
