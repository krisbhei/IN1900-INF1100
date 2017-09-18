# Regne ut arealet til rektangel gitt
# lengde l og bredde b fra bruker i commandline:

import sys

print(sys.argv)
# sys.argv[0] er navnet på fila

# Uten test:
#l = float(sys.argv[1])
#b = float(sys.argv[2])
#A = l*b

# Med test:
try:
    l = float(sys.argv[1])
    b = float(sys.argv[2])
except IndexError:
    # Vi må finne ut om l eller b mangler.
    # Siden det har oppstått en indekseringsfeil,
    # er det _garantert_ at b mangler (hvorfor?)

    # Kan gjøres ved å f.eks sjekke lengde til sys.argv,
    # og be bruker om å taste inn verdi til de manglede
    # størrelsene:
    if (len(sys.argv) == 1):
	l = float(input("l = "))
    b = float(input("b = "))

A = l*b
