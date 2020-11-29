import numpy as np
import math
"""
u1 = y
u2 = y'
u1' = u2
u2' = 3xu2 - 2u1 + 1.5

"""

class Shoot:
    def __init__(self, a, b, y0, y1, h, eps, alpha0, alpha1):
        self.a = 0.5
        self.b = 0.8
        self.y0 = 0.5
        self.y1 = 1.2
        self.h = h
        self.eps = eps
        self.alpha0 = alpha0
        self.alpha1 = alpha1

    def getAngle(self, a, b):
        return (a + b) / 2

    def rad(self, alpha):
        return alpha * math.pi / 180


    def getAns(self):
        while True:
            currAlpha = self.getAngle(self.alpha0, self.alpha1)

            u1 = []
            u1.append((self.y0 - math.tan(self.rad(currAlpha))) / 0.5)

            u2 = []
            u2.append(math.tan(self.rad(currAlpha)))

            prev = 0
            for x in np.arange(self.a + self.h, self.b, self.h):
                u1.append(u1[prev] + self. h * u2[prev])
                u2.append(u2[prev] + self.h * (3*x * u2[prev] - 2*u1[prev] + 1.5))
                prev += 1

            y1 = u2[prev]
            if math.fabs(y1 - self.y1) <= self.eps:
                return u1

            if y1 > self.y1:
                self.alpha1 = currAlpha
            else:
                self.alpha0 = currAlpha




