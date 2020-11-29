import numpy as np
import matplotlib.pyplot as plt


def booles_rule_origin(f, a, b):
    d_x = (b-a)/4
    intervals = np.arange(a, b+d_x, d_x)
    return 2 * d_x / 45 * (7 * f(intervals[0]) + 32 * f(intervals[1]) + 12 * f(intervals[2]) + 32 * f(intervals[3]) + 7 * f(intervals[4]))


def booles_rule(f, a, b, n):
    d_x = (b - a) / n * 5
    intervals = np.arange(a, b, d_x)
    result = 0
    for i in intervals:
        result += booles_rule_origin(f, i, min(i + d_x, b))
    return result


def plot_booles_origins(f, a, b):
    d_x = (b-a)/4
    intervals = np.arange(a, b , d_x)
    plt.plot(intervals, list(map(f, intervals)),
             '.', markersize=4, color="red")
    plt.title("Trapezoidal Rule")

def plot_booles_rule(f, a, b, n):
    d_x = (b - a) / (n - 1)
    intervals = list(np.arange(a, b + d_x, d_x))
    X = list(np.arange(a, b, 0.01))
    Y = list(map(f, X))
    plt.plot(X, Y, lw=3)
    plt.plot(intervals, list(map(f, intervals)),
             '.', markersize=8, color="red")
    for i in intervals:
        if i != b: plot_booles_origins(f, i, i + d_x)
        plt.plot([i, i], [0, f(i)], color='red')
    plt.title("Boole's Rule")
    plt.plot([a, b], [0, 0])