import matplotlib.pyplot as plt
import numpy as np

def f(x, t): # Function representing the differential equation
    return -x**3 + np.sin(t)

def euler(f, x0, t0, t_end, h):  # Euler's method implementation
    t = np.arange(t0, t_end + h, h)  # Create time points
    x = np.zeros_like(t)             # Initialize solution array
    x[0] = x0                        # Set the initial condition

    for i in range(1, len(t)):       # Calculate the solution iteratively 
        x[i] = x[i - 1] + h * f(x[i - 1], t[i - 1])

    return t, x

# Call the function with parameters
t, x = euler(f, 0, 0, 10, 0.01)

# Plotting the solution
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Euler's method")
plt.show()