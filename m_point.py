import math
class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
class Line(object):
    def __init__(self,p1,p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()
        self.len = math.sqrt(self.x*self.x + self.y*self.y)
    def get_len(self):
        print(self.len)
        return self.len
        #print(self.len)
p1 = Point(222222,23)
p2 = Point(25,27)

line = Line(p1,p2)
line.get_len()