import queue
import threading
import time
from tkinter import Tk, Canvas, Button



class Food():
    def __init__(self):
        self.new_food()
    def new_food(self):
        x = random.randrange(50,480,10)
        y = random.randrange(50,480,10)
        self.positon = x,y
        self.queue.put({'food':self.positon})
class Snake(threading.Thread):
    def __init__(self,world,queue):
        threading.Thread.__init__(self)
        self.world = world
        self.queue = queue
        self.points_earned = 0
        self.food = Food()
        self.snake_points = [(495,55),(485,55),(465,55),(455,55)]
        self.start()
    def run(self):
        if self.world.is_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.queue.put({'move':self.snake_points})
            time.sleep(1)
            self.move()
class World(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        self.canvas = Canvas(self,width=500,height=300,bg='red')
        self.canvas.pack()
        self.snake = self.canvas.create_line((0,0),(0,0),fill='black',width=10)
        self.food = self.canvas.create_rectangle(0,0,0,0,fill='#FFCC4C',outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(450,20,fill='white',text='SCORE:0')
        self.queue_handler()
    def queue_handler(self):
        while True:
            try:
                task = self.queue.get(block=False)
                if task.get('game_over'):
                    self.game_over()
                if task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake,*point)
            except queue.Empty:
                if not self.is_game_over:
                    self.canvas.after(100,self.queue_handler)
    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text('Game Over')
        qb = Button(self,text='Quit',command= self.destroy)
        rb = Button(self,text='Again',command= self.__init__)
if __name__ =="__main__":
    q = queue.Queue()
    world = World()
    snake = Snake(world,q)
    world.bind('<Key-Left>',snake.key_pressed)
    world.mainloop()
