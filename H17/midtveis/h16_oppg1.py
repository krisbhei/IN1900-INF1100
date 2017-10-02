# a
y = 4
n = 2
print(y**n)

# b
a = "All work and no play makes Jack a dull boy".split()
print(a[-2])

# c
A = [[-1,0,1],[0,0,3],[5,6,7]]
print(A[1][2])

# d
s = 0
for n in range(2):
    s = s + 3
print(s)

# e
A = ['5','6','7','end']
try:
    b = float(A[4])
except IndexError:
    print("A has length %d"%len(A))
except ValueError:
    print("Cannot convert '%s' to float"%A[4])

# f
F = [C*0.5 + 30 for C in range(5)]
print(F[-1])

# g
import numpy as np
a = [7,6]
b = [3,2]
a_array = np.array(a)
b_array = np.array(b)

print(a+b)
print(a_array + b_array)

# h
from numpy import *
v0 = 1.0
a = 1.0
t = linspace(0,1,3)
y = v0*t + a*t**2
for t_,y_ in zip(t,y):
    print("%4.2f %4.2f"%(t_,y_))

# i
def f(x):
    return x**3

def test_f():
    x = 2.0
    expected = 8.0
    computed = f(x)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = "expected %g, computed %g"%(expected,computed)
    assert success, msg
test_f() 

# j
def f(x):
    return 2*x
def g(y):
    return y+7
x = 7
print("the magic number is %g"%f(g(f(x))) )
