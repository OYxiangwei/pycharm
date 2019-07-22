class student():
    name = "OY"
    age = 11
    def study(self):
        self.name = "anonymous"
        self.age = 18
        print("my name is :{}".format(self.name))
        print("my age is :{}".format(self.age))
        print("我爱学习")
        return None
    def studyagain():
        print(__class__.name)
        print(__class__.age)
        print("调用绑定函数使用类名")
s = student()
s.study()
student.studyagain()
