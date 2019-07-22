import random


class Food():
    def __init__(self):
        self.new_food()
    def new_food(self):
        x = random.randrange(50,480,10)
        y = random.randrange(50,480,10)
        self.positon = x,y
        self.queue.put({'food':self.positon})
class Snake():
    def move(self):
        new_snake_point = self.cal_new_position()
        if self.food.positon == new_snake_point:
            self.point_earned += 1
            self.queue.put({"points_earned":self.points_earned})
            self.food.new_food()
        else:
            self.snake_points.pop()
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)
    def cal_new_position(self):
        last_x,last_y = self.snake_points[-1]
        if self.direction == 'Up':
            new_snake_point = last_x,last_y - 10
        elif self.direction == 'Down':
            new_snake_point = last_x,last_y + 10
        return new_snake_point
    def check_game_over(self,snake_point):
        x,y = snake_point[0],snake_point[1]
        if not -5 < x <505 or not -5 < y < 315:
            self.queue.put({'game_over':True})
s1 = Snake()
s1.move()