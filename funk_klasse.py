class Parabola:
    def __init__(self,c0,c1,c2):
        self.c0 = c0;self.c1 = c1;self.c2 = c2

    def __call__(self,x):
        c0 = self.c0;c1 = self.c1;c2 = self.c2
        return c0 + c1*x + c2*x*x

class Line(Parabola):
    def __init__(self,c0,c1):
        Parabola.__init__(self,c0,c1,0)


if __name__ == '__main__':
    l = Line(0,2)
    for x in range(10):
        print l(x)
