"""
Programmet finner n jevnt fordelte x-verdier i et intervall [a,b] der a < b.
I dette programmet er a,b og n tilfeldig valgt.
"""
a = 1
b = 2
n = 10

dx = (b-a)/(n-1) # deler på n-1 fordi for-løkken under går til n-1.
for i in range(n):
    x = a + i*dx
    print(x)
