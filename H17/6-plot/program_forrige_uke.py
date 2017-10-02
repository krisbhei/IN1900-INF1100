import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x + 1

def f2(x):
    return 2*x + 2

x_start = 1
x_end = 2
n = 11
x = np.linspace(x_start,x_end,n)

# Finn ut hva f er på *alle* x-verdier:
f_values = f(x)

# f_values er en liste der f har blitt brukt på hvert
# element i x-arrayet
print(f_values)

# Her tegnes begge grafene
plt.plot(x,f_values,x,f2(x))

# Siden vi har flere grafer, er det viktig å kunne skille på dem
plt.legend(["2x + 1","2x + 2"])

# Gi navn til aksene
plt.xlabel("her kan man skrive hva x representerer")
plt.ylabel("her kan man skrive hva y representerer")

# En tittel, hvis man har lyst
plt.title("dette er en tittel")

# For å vise fram grafene på skjerm
plt.show()
