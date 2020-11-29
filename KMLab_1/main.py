from trapezoidal_rule import *
from booles_rule import *
from runge import *
import math

def f(x):
    return math.cos(x**2)

a = 0
b = 1
n1 = 30
n2 = 20

print("Trapezoidal Rule: " + str(trapezoidal_rule(f, a, b, n1)))
print("error: " + str(runge_rule(f, a, b, n1, trapezoidal_rule, 1/3)))
plot_trapezoidal_rule(f, a, b, n1)
plt.show()
print("Boole's rule: " + str(booles_rule(f, a, b, 20)))
print("error: " + str(runge_rule(f, a, b, n2, booles_rule, 1/3)))
plot_booles_rule(f, a, b, 20)
plt.show()