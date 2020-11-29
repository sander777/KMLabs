import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return (x - 1) / (math.sinh(x)) ** 0.5

def print_function(f, a, b):
    x = list(np.arange(a, b, 0.01))
    y = list(map(f, x))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    print_function(lambda x: 1 / (math.sinh(x) ** 0.5), 0.01, 1)