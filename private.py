class person():
    name = "西北云天"
    __age = 12
    _hobby = "work"
p = person()
print(p.name)
print(person.__dict__)
print(p._person__age)
print(p._hobby)
