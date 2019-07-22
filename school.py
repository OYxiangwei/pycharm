course_list = []
class school(object):
    def __init__(self,school_name):
        self.school_name = school_name
        self.student_list = []
        self.teacher_list = []
        global course_list
    def hire(self,obj):
        self.teacher_list.append(obj.name)
        print("new teacher {0}".format(obj.name))
    def enroll(self,obj):
        self.student_list.append(obj.name)
        print("new students {0}".format(obj.name))
class grade(school):
    def __init__(self,school_name,grade_code,grade_course):
        super(grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        course_list.append(self.course)
        print("{0}现在有代号为{1}的课程{2}".format(self.school_name,self.code,self.course))

    def course_info(self):
        print("课程大纲{} 是 day1 , day 2 ,day3".format(self.course))
python = grade("unk",1,'python')
linux = grade('bjk',2,'linux')

class school_member(object):
    def __init__(self,name,age,sex,role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("i am {0} and i am a {1}".format(self.name,self.role))

stu_num_id = 00
class students(school_member):
    def __init__(self,name,age,sex,role,course):
        super(students, self).__init__(name,age,sex,role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + 's' + str(course.code) + str(stu_num_id).zfill(2)
        self.id = stu_id
        self.mark_list = {}
    def study(self,course):
        print("i come to study {0},my number is {1}".format(course.course,self.id))
    def pay (self,course):
        print("i pay 100 for {0}".format(course.course))
        self.course_list.append(course.course)
    def praise(self,obj):
        print("{0} think {1} is very good".format(self.name,obj.name))
    def mark_check(self):
        for i in self.mark_list.items():
            print(i)
    def out(self):
        print("i am out")
tea_num_id = 00
class Teacher(school_member):
    def __init__(self,name,age,sex,role,course):
        super(Teacher, self).__init__(name,age,sex,role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + 'T' + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id
    def teach(self,course):
        print("i come to teach {0},my id is {1}".format(course.course,self.id))
    def record_mark(self,Date,course,obj,level):
        obj.mark_list["Day"+Date] = level
a = students('文宸',1,"male","student",python)
python.enroll(a)
a.study(python)
a.pay(python)
t = Teacher('祥伟',18,"male",'teacher',python)
python.hire(t)
t.teach(linux)
t.record_mark('1',linux,a,"A")
print(a.course_list)
a.praise(t)