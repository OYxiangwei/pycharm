class student():
    name = "OY"
    age = 11
    def study(self):
        self.name = "anonymous"
        self.age = 18
        print("我爱学习")
        return None
print(student.name)
print(student.age)
print("*"*20)
print(id(student.name))
print(id(student.age))
print("*"*20)
s = student()

s.study()
print(student.__dict__)
print(s.__dict__)
s.name = "xxxxx"
s.age = 111111
print(s.__dict__)
print(s.name)
print(s.age)
print(id(s.name))
print(id(s.age))