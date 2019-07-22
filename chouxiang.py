class animal():
    def sayhill(self):
        print("every is ")
class dog(animal):
    def sayhill(self):
        print("wangwangwang...")
class person(animal):
    def sayhill(self):
        print("welcome to here")

d = dog()
d.sayhill()
p = person()
p.sayhill()
a = animal()
a.sayhill()