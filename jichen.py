class person ():
    name = "None"
    age = 25
    __score = 0
    _petname = "xh"
    def sleep(self):
        print("sleep_____")
    def work(self):
        print("enjoy life")
class teacher(person):
    teacher_id = 9527
    name = "truename"
    def maketest(self):
        print("考试开始")
    def work(self):
        print("好好教书")
        #person.work(self)
        super().work()
        self.maketest()
t = teacher()
print(t.name)
print (t._petname)
t.maketest()
print(t.teacher_id)
t.work()