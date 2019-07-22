class tulingMetaclass(type):
    def __new__(cls,name,bases,attrs):
        print("tuling..")
        attrs["id"] = '00000'
        attrs["addr"] = 'beijing'
        return type.__new__(cls,name,bases,attrs)
class teacher(object,metaclass=tulingMetaclass):
    pass
t = teacher()
print(t.id)
print(t.addr)