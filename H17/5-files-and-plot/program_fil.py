# Lage en fil:

# 1) (man slipper å huske å lukke fila med with)
x = [1,2,3,4]
with open("testfil1.dat","w") as outfile:
    outfile.write("x:\n")
    for x_val in x:
        outfile.write("%d "%x_val)

# 2)
outfile = open("testfil2.dat","w")
outfile.write("x:\n")
for x_val in x:
    outfile.write("%d "%x_val)
outfile.close() # <- denne er viktig å huske hvis man bruker denne metoden!!


# Lese en fil:

# 1)
x1 = []
with open("testfil1.dat","r") as infile:
    infile.readline()
    for line in infile: # <- Fint å bruke hvis man ikke vet på
                        # forhånd hvor mange lijer det er i fila
        x_values = line.split() # <- x_values er nå en liste av ord fra line
        for x_val in x_values:
            x1.append(float(x_val))

# 2)
x2 = []
infile = open("testfil2.dat","r")
infile.readline()
for line in infile:
    x_values = line.split() # <- x_values er nå en liste av ord fra line
    for x_val in x_values:
        x2.append(float(x_val))

print(x1,x2)
