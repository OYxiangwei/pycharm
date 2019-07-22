import random
import math
num = input("请输入一个三位数：")
def save():
    str_num = ''
    for i in range(4):
        num = random.randrange(97,123)
        str_s = chr(num)
        str_num = str_num + str_s
def line():
    str_num = ''
    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num + str(num)
    return str_num

random_num = random.randrange(100,1000)
print(random_num)
if num.isdigit() and 100<int(num)<1000:
    num = int(num)
    random_num = int(random_num)
    if num > random_num:
        bai = num//100
        shi = num%100//10
        ge = num%10
        print("这个三位数的百位{0}-十位{1}-个位{2}".format(bai,shi,ge))
    if num < random_num:
        for i in range(10):
            str_line = line()
            with open('str_num.txt','a') as f:
                f.write(str_line+'\n')

    if num == random_num:
        print("yes")
else:
    print("请按规定输入")
