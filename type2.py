def talk(self):
    print("talk...")
def say(self):
    print("say......")

A = type("Aname",(object,),{"class_talk":talk,"class_say":say})
a = A()
a.class_talk()