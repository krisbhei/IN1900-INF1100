import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x + 3)

n = 10000 # valg av antall punkter i intervallet har mye å si!
x_small = np.linspace(1e-2,10,n)
x_large = np.linspace(1e2,1e3,n)

f_small = f(x_small)
f_large = f(x_large)

plt.title("D:")
plt.plot(x_small,f_small,x_large,f_large)
plt.legend(["liten x","stor x"])
plt.xlabel("x")
plt.ylabel("f(x)")

#men det finnes plt.figure() som lager nye vinduer!
plt.figure()
plt.plot(x_small,f_small)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f for små verdier av x")

plt.figure()
plt.plot(x_large,f_large)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f for store verdier av x")

plt.show()
