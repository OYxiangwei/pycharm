class person():
    def eat(self):
        print(self)
        print("eat>>")
    @classmethod
    def play(cls):
        print(cls)
        print("play.....")
    @staticmethod
    def say():
        print("say.....")
oy = person()
oy.eat()
person.play()
person.say()
oy.play()
oy.say()
