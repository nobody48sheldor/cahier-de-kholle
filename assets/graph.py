import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 1.5, 400)
Y = []
T = np.linspace(0, X[-1]*np.exp(X[-1]), 400)

for x in X:
    Y.append(x*np.exp(x))

plt.plot(X, Y, '-')
plt.plot(T, T, '-')
plt.plot(Y, X)
plt.savefig("graph-kholle-W.png")
plt.show()
