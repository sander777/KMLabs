import math
import numpy as np
import matplotlib.pyplot as plt

ALPHA = 3
BETA = 1.9
# y' = -a * b * t * y t(a) = b


class RungeKutta:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def f(self, t, y):
        return -self.a*self.b * t * y

    def calculate(self):
        res = list()
        ti = self.a
        yi = self.b
        res.append(yi)
        while ti != self.a + 3:
            k1 = self.h * self.f(ti, yi)
            k2 = self.h * self.f(ti + self.h/2, yi + k1/2)
            y = yi + k2
            res.append(y)
            ti += self.h
            yi = y
        return res


class TaylorSeriesMethod:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def der1(self, t, y):
        return -self.a * self.b * t * y

    def der2(self, t, y):
        return -self.a * self.b * y - self.a * self.b * t * self.der1(t, y)

    def der3(self, t, y):
        return -2 * self.a * self.b * self.der1(t, y) - self.a * self.b * t * self.der2(t, y)

    def der4(self, t, y):
        return -3 * self.a * self.b * self.der2(t, y) - self.a * self.b * t * self.der3(t, y)

    def calcY(self, t, h, y):
        res = y
        d = list()
        d.append(self.der1(t, y))
        d.append(self.der2(t, y))
        d.append(self.der3(t, y))
        d.append(self.der4(t, y))

        for i in range(len(d)):
            res += d[i]*math.pow(h, i+1)/math.factorial(i+1)
        return res

    def calculate(self):
        res = list()
        t = self.a
        y = self.b
        res.append(y)

        while t != self.a + 3:
            y = self.calcY(t, self.h, y)
            res.append(y)
            t += self.h
        return res


class ABM:
    def __init__(self, a, b, h, y0, y1, y2, y3):
        self.a = a
        self.b = b
        self.h = h

    def f(self, t, y):
        return -self.a * self.b * t * y

    def calculate(self):
        tl = TaylorSeriesMethod(self.a, self.b, self.h)
        res = tl.calculate()
        self.y0 = self.b
        self.y1 = res[1]
        self.y2 = res[2]
        self.y3 = res[3]

        t = list()
        k = 0
        for i in np.arange(self.a, self.a + 3 + self.h, self.h):
            t.append(i)
            k += 1

        for i in range(4, len(t)):
            p = self.y3 + self.h/24 * (-9 * self.f(t[i-4], self.y0) + 37 * self.f(t[i-3], self.y1) -
                                       59*self.f(t[i-2], self.y2) + 55*self.f(t[i-1], self.y3))
            y = self.y3 + self.h/24 * (self.f(t[i-3], self.y1) - 5 * self.f(t[i-2], self.y2) +
                                       19 * self.f(t[i-1], self.y3) + 9*self.f(t[i], p))
            self.y0 = self.y1
            self.y1 = self.y2
            self.y2 = self.y3
            self.y3 = y

        return res


if __name__ == '__main__':
    for i in range(0, 3):
        h = 1 / (2**i)
        rk = RungeKutta(ALPHA, BETA, h)
        y = rk.calculate()
        x = list(np.arange(ALPHA, ALPHA + 3 + h, h))
        plt.plot(x, y, 'ro')
        plt.plot(x, y)
        plt.title("Метод Рунге-Кутта N = 2 h = " + str(h))
        plt.show()

        ts = TaylorSeriesMethod(ALPHA, BETA, h)
        y = ts.calculate()
        plt.plot(x, y, 'ro')
        plt.plot(x, y)
        plt.title("Метод рядів Тейлора h = " + str(h))
        plt.show()

        abm = ABM(ALPHA, BETA, h, y[0], y[1], y[2], y[3])
        y = abm.calculate()
        x = list(np.arange(ALPHA, ALPHA + 3 + h, h))
        plt.plot(x, y, 'ro')
        plt.plot(x, y)
        plt.title("Метод Адамса-Бешфорса-Маултона h = " + str(h))
        plt.show()