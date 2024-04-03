# @title Trapezoid Function

import numpy as np

def trapezoid(f,a,b,N=500):
    x = np.linspace(a,b,N+1)
    y = f(x)

    y_right = y[1:] # Right endpoints
    y_left = y[:-1] # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

trapezoid(np.sin,0,np.pi/2)