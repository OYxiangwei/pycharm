class student():
    name = "OY"
    age = 11
    def study(self):
        self.name = "anonymous"
        self.age = 18
        print("我爱学习")
        return None

oy = student()
print(oy.name)
print(oy.age)
oy.study()
print(oy.name)
print(oy.age)