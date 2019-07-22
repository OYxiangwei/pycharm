class A():
    pass
def say(self):
    print("dddd")
class B():
    def say2(self):
        print("dddddddddd222222")

say(9)
A.say = say
a = A()
a.say()
b = B()
b.say2()