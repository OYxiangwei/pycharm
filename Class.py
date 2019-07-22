class person():
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("sleep>>>>")
class fish():
    def __init__(self,name):
        self.name=name
    def swim(self):
        print("swim>>")
class bird():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print("fly>>>>")
class superman(person,fish,bird):
    def __init__(self,name):
        self.name=name
class woman(person,bird):
    def __init__(self,name):
        self.name=name
    def shipping(self):
        print("i like shipping")

s =superman("oy")
s.fly()
s.swim()
s.sleep()
print(s.name)
w = woman("kit")
w.shipping()
w.sleep()
w.fly()