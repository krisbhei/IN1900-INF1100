class Person:
    def __init__(self,navn):
        self.navn = navn

    def __call__(self,x):
        print("%s sier %s fra __call__!"%(self.navn,x))

    def maser(self,noe):
        print("%s sier %s"%(self.navn,noe))
        self(noe)

class Student(Person):
    def __init__(self,navn,studie):
        # Dette:
        Person.__init__(self,navn)
        # er helt det samme som om det stod:
        # self.navn = navn

        self.studie = studie

    def __call__(self,x):
        Person.__call__(self,x)
        print("%s studerer %s"%(self.navn,self.studie))

if __name__ == '__main__':
    p = Person('En person')
    p('hei')

    s = Student('Harry p','AST2000')
    s.maser('halla')
