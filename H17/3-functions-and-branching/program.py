def funksjon(a,b):
    # Løser a*x + b = 0
    x = -b/a
    return x

# Funker også: funksjon = lambda a,b: -b/a

def test_funksjon():
    # Ved regning, vil x + 2 = 0 gi at x = -2
    a = 1
    b = 2
    forventet = -2
    svar = funksjon(a,b)
    grense = 1e-14
    test = abs(svar - forventet) < grense

    # Nå sjekker programmet om test er sann ved bruk av assert.
    # Hvis test ikke er sann, skrives ut meldingen etter test.
    assert test, "Forventet: %g, fikk: %g!"%(forventet,svar)

test_funksjon() # Når alt stemmer, skal det ikke skrives ut noe i testfunksjonen.
                # Husk å kalle på testfunksjonene i programmene dine!

def funksjon2(linjer):
    # Funksjonen finner skjæringspunktet x mellom to linjer:
    # a1*x + b1 = a2*x + b2

    linje1 = linjer[0] # henter ut (a1,b1)
    linje2 = linjer[1] # henter ut (a2,b2)

    a1 = linje1[0]; b1 = linje1[1]
    a2 = linje2[0]; b2 = linje2[0]

    x = (b2 - b1)/(a1 - a2)

    f1 = a1*x + b1
    f2 = a2*x + b2

    return x,f1,f2

a1 = 1
b1 = 2
l1 = (a1,b1)

a2 = -1
b2 = 3
l2 = (a2,b2)

lst = [l1,l2]
x,svar1,svar2 = funksjon2(lst)
print("x %8s %6s"%("linje1","linje2"))
print("%.2f %3.2f %3.2f"%(x, svar1,svar2))
