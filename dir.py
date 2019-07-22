class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setname(name)
    def intro(self):
        print("hi,my name is : {}".format(self.name))
    def setname(self,name):
        self.name=name.upper()
s1 = student("sTlong",12)
s2 = student("luoda",11)
s1.intro()
s2.intro()