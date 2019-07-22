class student():
    name = "OY"
    age = 11
    def study(self):
        print("我爱学习")
        return None

oy = student()
oy.name = "hacker"
print(oy.name)
oy.study()
print(student.__dict__)
print(oy.__dict__)

