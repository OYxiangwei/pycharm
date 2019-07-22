class A():
    pass
class B(A):
    pass
class C(B):
    """"zheswend"""
    name = "n"
    pass
print(issubclass(B,A))
print(issubclass(A,object))
c = C()
print(isinstance(c,C))
print(isinstance(A,A))
print(hasattr(c,"age"))
help(setattr)
print(setattr(c,"age",11))
print(c.age)
dir(C)
print(C.__dict__)
print(C.__doc__)
print(C.__name__)
print(C.__bases__)