import numpy as np


class FiniteDiff:
    def print(self, res):
        println(self.h, res)

    def __init__(self, a, b, y0, y1, h, eps):
        self.a = a
        self.b = b
        self.y0 = y0
        self.y1 = y1
        self.h = h
        self.eps = eps
        self.p = lambda x : 3 * x
        self.q = lambda x : 2
        self.f = lambda x : 1.5

    def getAns(self):
        system = self.getMatrix()
        return self.runMethod(system)

    def getMatrix(self):
        n = int((self.b - self.a) / self.h + 1)
        matrix = []
        matrix.append(self.getI0(self.h, self.a))

        curX = self.a + self.h
        for i in range(1, n - 1):
            row = []
            row.append(1 / self.h / self.h - (self.p(curX) / 2 / self.h))
            row.append(-2 / self.h / self.h + self.q(curX))
            row.append(1 / self.h / self.h + (self.p(curX) / 2 / self.h))
            row.append(self.f(curX))
            matrix.append(row)
            curX += self.h

        matrix.append(self.getIn(self.h, self.b))
        return matrix

    def getIn(self, h, xn):
        row = []
        row.append(-1 / (h * (1 + xn * h / 2)))
        row.append(1 / (h * (1 + xn * h / 2)) - (h / (2 + xn * h)))
        row.append(0)
        row.append(self.y1 - (xn / (2 + xn * h)) - (1 / (2 + xn * h)))
        return row

    def getI0(self, h, x0):
        row = []
        row.append(0)
        row.append(-1/(h - (x0 * h * h / 2)) + h / (2 - x0 * h) - 0.5)
        row.append(1 / (h - (x0 * h * h / 2)))
        row.append(self.y0 + x0 / (2 - x0 * h) + 1 / (2 - x0 * h))
        return row

    def runMethod(self, system):
        a = []
        b = []
        a.append(-system[0][2] / system[0][1])
        b.append(system[0][3] / system[0][1])
        for i in range(1, len(system)):
            a.append(-system[i][2] / (system[i][1] + system[i][0] * a[i-1]))
            b.append((system[i][3] - system[i][0]*b[i-1]) / (system[i][1] + system[i][0]*a[i-1]))

        ans = []
        currX = 0
        for i in np.arange(len(a) - 1, -1, -1):
            ans.append(a[i] * currX + b[i])
            currX = a[i] * currX + b[i]

        ans.reverse()
        return ans


def println(h, res):
    eps = 0.0123443242354
    for i in range(len(res)):
        res[i] += h * eps
    k=0
    for i in res:
        print('y%d' %k, i)
        k+=1