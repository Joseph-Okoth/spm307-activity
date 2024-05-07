import matplotlib.pyplot as plt
import numpy as np

def f(x, t):
    return -x**3 + np.sin(t)

def rk4(f, x0, t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    x = np.zeros_like(t)
    x[0] = x0

    for i in range(1, len(t)):
        k1 = h * f(x[i - 1], t[i - 1])
        k2 = h * f(x[i - 1] + k1/2, t[i - 1] + h/2)
        k3 = h * f(x[i - 1] + k2/2, t[i - 1] + h/2)
        k4 = h * f(x[i - 1] + k3, t[i - 1] + h) 
        x[i] = x[i - 1] + (k1 + 2*k2 + 2*k3 + k4) / 6 

    return t, x

t, x = rk4(f, 0, 0, 10, 0.01)
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Fourth-order Runge-Kutta method")
plt.show()
