class A():
    def __init__(self,name=0):
        print("被调用  ")
    def __call__(self):
        print("call被调用")
a = A()
a()
#对象当函数使用时触发
