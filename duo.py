from pkg1 import *
from types import MethodType

s = student("liusha",21)
s.say()
s.sayhill = MethodType(sayhill,student)
s.sayhill()