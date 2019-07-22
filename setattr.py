class person():
    def __init__(self):
        pass
    def __setattr__(self,name,value):
        print("设置属性: {0}".format(name))
        #self.name = value
        super().__setattr__(name,value)
p = person()
print(p.__dict__)
p.age = 18
p.name = "lllll"
print(p.name)
print(p.age)