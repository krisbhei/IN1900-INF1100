class Person:
    def __init__(self,navn):
        self.navn = navn
    def __call__(self,x):
        print "%s sier %s fra __call__!"%(self.navn,x)

    def sier(self,x):
        self(x)

class Student(Person):
    def __init__(self,navn,studie):
        Person.__init__(self,navn)
        self.studie = studie

    def __call__(self,x):
        Person.__call__(self,x)
        print "%s studerer %s"%(self.navn,self.studie)

if __name__ == '__main__':
    # p = Person('harry p')
    # p('hei')
    s = Student('harry potter','svart magi, ogsaa kalt algebra')
    s.sier('halla')
