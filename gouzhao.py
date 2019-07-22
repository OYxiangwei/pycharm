class person():
    def __init__(self):
        self.name="noname"
        self.age = 18
        self.address = "hepingroad"
        print("in init function")

p = person()
p.name = "hacker"
print(p.address)

