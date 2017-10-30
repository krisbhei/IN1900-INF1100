from math import pi
class Circle:
    def __init__(self,x0,y0,R): # <- For å sende inn informasjon
        self.x0 , self.y0, self.R = x0,y0,R

    def __str__(self): # <- For å kunne skrive ut ønska informasjon når vi bruker print
        return "En sirkel med radius = %g og sentrum i (%g,%g)"\
        %(self.R,self.x0,self.y0)

    def __call__(self,x,y): # <- For å kalle direkte på en sirkel
        print((self.x0 - x)**2 + (self.y0 - y)**2 <= self.R**2)

    def area(self):
        return pi*self.R**2

    def circumference(self):
        return 2*pi*self.R


if __name__ == '__main__':

    # Bruke __init__ ved å sende inn informasjon
    c1 = Circle(0,1,2)

    # Bruke __call__:
    c1(2,3)

    # Bruke __str__:
    print(c1)

    # Definere testfunksjon. Kan også defineres før if-testen
    def test_circle():
        c = Circle(0,0,1)
        tol = 1e-14

        expected_area = pi
        comp_area = c.area()

        assert abs(expected_area-comp_area) < tol, "Expected: %g, got:%g"%(expected_area,comp_area)

        expected_circ = pi*2
        comp_circ = c.circumference()

        assert abs(expected_circ-comp_circ) < tol, "Expected: %g, got:%g"%(expected_circ,comp_circ)

    test_circle()
else: # Else er bare ment for å demonstrere. Dette er ikke god praksis generelt.
    print('Circle-modulen har blitt importert')
