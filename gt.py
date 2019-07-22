class student():
    def __init__(self,name):
        self.name = name
    def __gt__(self,obj):
        print("哈哈，{0}会比{1}大吗".format(self.name,obj.name))
        return self.name > obj.name
stu1 = student("one")
stu2 = student("two")
print(stu1 > stu2)