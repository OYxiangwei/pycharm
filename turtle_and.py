import random as r
class Turtle(object):
    def __init__(self):
        self.power = 100
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        new_x = r.choice([1,2,-1,-2]) + self.x
        new_y = r.choice([1,2,-1,-2]) + self.y
        if new_x < 0:
            self.x = 0 -(new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y >10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        self.power -= 1
        return (self.x,self.y)
    def eat(self):
        self.power += 20
        if self.power >=100:
            self.power = 100
class Fish(object):
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x >10:
            self.x = 10 - (new_x - 10 )
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y >10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        return(self.x,self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)
while True:
    if not len(fish):
        print("鱼被吃完了")
        break
    if not turtle.power:
        print("乌龟体力耗尽")
        break
    pos = turtle.move()
    for each_fish in fish:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼鱼被吃了")