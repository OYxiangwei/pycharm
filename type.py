from types import MethodType
class A():
    pass
def say(self):
    print("one")
a = A()
a.say=MethodType(say,A)
a.say()
