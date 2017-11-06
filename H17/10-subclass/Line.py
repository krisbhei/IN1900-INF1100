import numpy as np
class Line:
    def __init__(self,c0,c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self,x):
        return self.c0 + x*self.c1

    def table(self,L,R,n):
        s = ""
        for x in np.linspace(L,R,n):
            y = self(x)
            s += "%g %g\n"%(x,y)
        return s

class Parabola(Line):
    def __init__(self,c0,c1,c2):
        Line.__init__(self,c0,c1)
        self.c2 = c2

    def __call__(self,x):
        return Line.__call__(self,x) + self.c2*x**2
