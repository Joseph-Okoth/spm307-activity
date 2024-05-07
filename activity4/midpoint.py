import matplotlib.pyplot as plt
import numpy as np

def f(x, t): 
    return -x**3 + np.sin(t)

def midpoint(f, x0, t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    x = np.zeros_like(t)
    x[0] = x0

    for i in range(1, len(t)):
        k1 = f(x[i - 1], t[i - 1])                # Slope at the beginning of the interval
        k2 = f(x[i - 1] + h/2 * k1, t[i - 1] + h/2)  # Slope at the midpoint
        x[i] = x[i - 1] + h * k2                   # Update the solution using midpoint slope

    return t, x

t, x = midpoint(f, 0, 0, 10, 0.01) 
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Midpoint method")
plt.show()