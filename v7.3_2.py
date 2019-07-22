import random

score = 0
total = 0
while 1:
    num = input("请输入1,2,3，三个数，输入-1结束：")
    total += 1
    if num == '-1':
        break
    rand_num = random.randrange(1,4)
    num = int(num)
    rand_num = int(rand_num)
    if num > rand_num:
        print("da")
    elif num == rand_num:
        score += 100
        print("得分是{}".format(score))
        print("概率是{}".format(score/100/total))
    elif num < rand_num:
        print("xiao")
