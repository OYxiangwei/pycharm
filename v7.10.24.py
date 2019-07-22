import re

s = 'i 22love 33you\n but you don\'t love \nme'
print(re.findall(r"\w+",s,re.M))
