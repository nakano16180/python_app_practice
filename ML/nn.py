import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return (x > 0).astype(np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.01)
#y = step_function(x)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.grid(True)

plt.yticks([-0.5, 0.0, 0.5, 1.0, 1.5])

plt.show()