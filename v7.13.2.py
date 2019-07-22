import itertools as its                    #调用循环迭代模块itertools

words ="abcdefghijklmnopqrstuvwxyz1234567890"                  #将所需要的元素赋值给words变量

r =its.product(words,repeat=12)      #元素在迭代器its中循环5次
#print(type(r))
dic=open("pass3.txt","a")                #将生成的密码存入文档pass.txt中

for i in r:                                        #采用循环的方式将密码输入到文档中

        dic.write(" ".join(i))

        dic.write("".join("\n"))            #将密码进行分行处理

dic.close()