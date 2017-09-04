# Lager to tomme lister:
liste1 = []
liste2 = []

N = 5 # Antall verdier osm settes i listene

liste4 = []
for i in range(N):
    v1 = i
    v2 = 2*i
    liste1.append(v1)
    liste2.append(v2)
    
    # Setter inn en liste i liste4
    liste4.append([v1,v2])

print("liste4:",liste4)
print("liste4[1]:",liste4[1])
print("liste4[1][0]:",liste4[1][1])
print("---")

liste3 = [liste1,liste2]
print("liste3:",liste3)
print("liste3[1]:",liste3[1])
print("liste3[1][0]:",liste3[1][1])
print("---")

# Henter ut ett og ett element fra liste1 og liste2
for fra_liste1,fra_liste2 in zip(liste1,liste2):
    print(fra_liste1,fra_liste2)

print("---")
a = 0
while(a <= 10):
    print(a)
    a += 1 # Hvorfor er denne linja viktig?
