class A():
    def __init__(self,name=0):
        print("被调用  ")
    def __call__(self):
        print("call被调用")
    def __str__(self):
        return "tuling"
a = A()
print(a)
