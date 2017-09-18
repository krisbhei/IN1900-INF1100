# Regne ut arealet til rektangel gitt
# lengde l og bredde b fra bruker:

import sys

l = float(input("l = "))
b = float(input("b = "))

if l < 0 or b < 0:
    sys.exit(1) # avslutt program

A = l*b
print(A)
