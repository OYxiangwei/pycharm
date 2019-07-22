class A():
    name = "oy"
    age = 12
    def __init__(self):
        self.name = "aaaa"
        self.age = 111
    def say(self):
        print(self.name)
        print(self.age)
class B ():
    name = "bbbb"
    age =3333
a = A()
a.say()
A.say(a)
A.say(A)
A.say(B)
