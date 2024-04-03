import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5,1.5,100)
y = np.exp(-x**2)

plt.plot(x,y)

x0 = 0
x1 = 1

y0 = np.exp(-x0**2)
y1 = np.exp(-x1**2)

plt.fill_between([x0,x1],[y0,y1],color='gray',alpha=0.5) # alpha is the transparency

plt.xlim(-0.5,1.5)
plt.ylim(0,1.1)

plt.show()