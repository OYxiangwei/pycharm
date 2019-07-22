class person():
    def fget(self):
        print("获取")
        return self._name * 2
    def fset(self,name):
        print("设置")
        self._name = name.upper()
    def fdel(self):
        print("删除")
        self.name="none"
    name = property(fget, fset, fdel)
p = person()
p.name = "ll"
print(p.name)
del(p.name)