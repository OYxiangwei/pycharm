class person():
    name = "hacker"
    age = 18
    def eat(self):
        print("eat___")
    def drink(self):
        print("drink___")
    def sleep(self):
        prinr("sleep>>>>")

class teacher(person):
    def work(self):
        print("work........")
class student(person):
    def sutdy(self):
        print("study.....")
class tutor(teacher,student):
    pass
t = tutor()
print(tutor.__mro__)
print(t.__dict__)
print(tutor.__dict__)
print("*"* 20)
class teacherMixin():
    def work(self):
        print("work****")
class studentMixin():
    def study(self):
        print("study*****")
class tutorM(person,teacherMixin,studentMixin):
    pass
tt = tutorM()
print(tutorM.__mro__)
print(tt.__dict__)
print(tutorM.__dict__)