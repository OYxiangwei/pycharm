
class anim():
    def __init__(self,name):
        print("name is  : {}".format(name))
class paxing(anim):
    pass
class dog(paxing):
    pass
class cat (paxing):
    pass
a = dog("kk")
c = cat("mimi")