class A():
    name = "noname"
    age = 12
    def __getattr__(self,name):
        print("mei")
        print(name)
        return 0
a = A()
print(a.name)
print(a.addr)
