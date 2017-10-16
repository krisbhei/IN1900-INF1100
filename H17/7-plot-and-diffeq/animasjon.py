import numpy as np
import matplotlib.pyplot as plt

# Anta S fra oppg. 3.21 er tilgjengelig som funksjon.

ts = np.linspace(0,2*np.pi,1000)
ns = np.linspace(1,100,100)

lines = plt.plot(ts,S(ts,ns[0])) # Hente ut linjene som vi plotter med
for n in ns:
    lines[0].set_ydata(S(ts,n)) # oppdater linjer
    plt.draw() # vis fram linjene
    plt.pause(0.05) # se de nye linjene i 0.05 sekunder
