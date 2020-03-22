#this program will plot three functions on the same set of axes

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4.0, 100)

y1 = x

y2 = x**2

y3 = x**3

plt.plot(x, y1, label= "f(x)=x")
plt.plot(x, y2, label= "Squared")
plt.plot(x, y3, label= "Cubed")

plt.legend()

plt.title("Weekly task 8 plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()