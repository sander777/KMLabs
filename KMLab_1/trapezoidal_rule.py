import numpy as np
import matplotlib.pyplot as plt


def trapezoidal_rule(f, a, b, n):
    d_x = (b-a)/(n-1)
    intervals = list(np.arange(a, b+d_x, d_x))
    intervals.pop()
    result = f(intervals.pop(0)) + f(intervals.pop(len(intervals) - 1))
    for i in range(len(intervals)):
        result += 2 * f(intervals[i])

    return result * d_x / 2


def plot_trapezoidal_rule(f, a, b, n):
    d_x = (b-a)/(n - 1)
    intervals = list(np.arange(a, b + d_x, d_x))
    X = list(np.arange(a, b, 0.01))
    Y = list(map(f, X))
    plt.plot(X, Y, lw=3)
    plt.plot(intervals, list(map(f, intervals)),
             '.', markersize=12, color="red")
    plt.plot(intervals, list(map(f, intervals)), color='red')
    for i in intervals:
        plt.plot([i, i], [0, f(i)], color='red')
    plt.title("Trapezoidal Rule")
    plt.plot([a, b], [0, 0])
