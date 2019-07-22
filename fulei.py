class A():
    def __init__(self):
        print("a")
class B(A):
    def __init__(self,name):
        print("b")
        print(name)
class C(B):
    def __init__(self,name):
        #B.__init__(self,name)
        super(C,self).__init__(name)
        super
        print("this is C addfunction")

c = C("oy")
