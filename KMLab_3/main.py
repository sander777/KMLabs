from Shoot import *
from FiniteDiff import *
import numpy as np
import matplotlib.pyplot as plt

import math
"""
[0.5; 0.8]
y'' -3xy' - 2y = 1.5
0.5y(1) + y'(1) = 2 // y0 = 2
y'(0.7) = 1.3 // y1 = 1.3


"""
EPS = 1e-6
H = 1e-2
Y0 = 2
Y1 = 1.3
ALPHA0 = 0
ALPHA1 = 45
A = 0.7
B = 1

if __name__ == '__main__':
    shoot = Shoot(A, B, Y0, Y1, H, EPS, ALPHA0, ALPHA1)
    result = shoot.getAns()
    x = list(np.arange(A, B, (B - A) / len(result)))
    plt.plot(x, result)
    plt.title("Методо пристрілки")
    plt.show()
    print("Shoot method")
    k = 0
    for i in result:
        print('y%d' %k,  i)
        k += 1

    finite = FiniteDiff(A, B, Y0, Y1, H, EPS)
    print("\nFinite difference method")
    rеsult = finite.getAns()
    finite.print(result)
    plt.plot(x, result)
    plt.title("Методо скінчених різниць з використання метода прогонки")
    plt.show()