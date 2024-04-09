import numpy as np

def f(x):
  # Defines the function f(x) = 5e^(-x) + x - 5.
  return 5 * np.exp(-x) + x - 5

def binary_search(a, b, tol):
  """
  Solves f(x) = 0 using binary search within the interval [a, b] with tolerance tol.

  Args:
      a: Lower bound of the search interval.
      b: Upper bound of the search interval.
      tol: Tolerance for convergence.
  """
  while abs(b - a) > tol:  # Continue until the interval is smaller than tolerance
    mid = (a + b) / 2       # Calculate the midpoint of the current interval
    if f(a) * f(mid) < 0:    # Check if root lies between a and mid (opposite signs)
      b = mid                # Update upper bound to the midpoint
    else:                    # Root lies between mid and b
      a = mid                # Update lower bound to the midpoint
  return (a + b) / 2  # Return the approximate solution (average of final interval)

# Constants
a = 0.5  # Adjusted initial guess for lower bound (can be further refined)
b = 2    # Adjusted initial guess for upper bound
tol = 1e-6  # Tolerance for convergence

# Solve using binary search
solution = binary_search(a, b, tol)

if solution is not None:
  print("Approximate solution of 5e^(-x) + x - 5 = 0 is:", solution)
else:
  print("Solution not found within the specified interval and tolerance.")
