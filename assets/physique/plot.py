import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,100,500)

k = 2
M = 1100

def func(x):
    value = 0.1*(1+ 2*np.sqrt(k/M)*x) * np.exp(-2*np.sqrt(k/M)*x)
    return(value)


Y = func(X)

plt.plot(X,Y)
plt.savefig("plot.png")
