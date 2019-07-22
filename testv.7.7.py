"""a = 5555
def Sum():
    global a
    a = 22
    pass
    print(a)

Sum()
"""

"""
print(sum(range(1,101)))
"""

"""import os,sys,time,datetime,re,math"""

"""d = {"a":1,"b":2,"c":3}
d2 = {"d":4,"e":5}
del d["a"]
d.update(d2)
d.setdefault("f",6)
print(d)"""

"""l = [1,1,1,2,3,3,4]
s = set(l)
l = [i for i in s]
print(l)"""

"""def info(*args,**kwargs):
    for k in args:
        print(k,end=" ")
    for k,v in kwargs.items():
        print(k,"-",v,end=" ")
info('oy',18,name="欧阳文宸")"""

"""print(type(range(100)))"""

"""f = open('str_num.txt','w')
try:
    f.write("hello,world")
except:
    print("错误")
finally:
    f.close()"""

"""def pow(m):
    return m*m
l = [1,2,3,4,5]
l2 = map(pow,l)
l = [i for i in l2 if i>10]
print(l)"""

"""import random
import numpy as np
print(random.randint(1,100))
print(random.random())
print(np.random.randn(5))"""
"""import re
str = '<div class ="nm">文宸</div>'
pattern = r'<div class =".*">(.*?)</div>'
print(re.findall(pattern,str))"""

"""a = 3
assert(a>1)
print("成功")"""

"""select distinct name from student"""

"""for i in range(10):
    try:
        if i < 5:
            print(i)
        else:
            raise Exception("大于等于5")
    except Exception as e:
        print(e)"""

"""s = '<a>呵呵</a><a>哈哈</a>'
import re
print(re.findall(r'<a>(.*)</a>',s))
print(re.findall(r'<a>(.*?)</a>',s))"""

"""l = [[1,2],[3,4],[5,6]]
l2 = [j for i in l for j in i]
print(l2)
import numpy
print(numpy.array(l).flatten().tolist())"""

"""x = "*"
y = "def"
z = ["d","e","f"]
print(x.join(y))
print(x.join(z))"""

"""a = input("请输入被除数:")
a = int(a)
try:
    ret = 100 / a
except Exception as e:
    print(e)
else:
    print("积是%d"%ret)
finally:
    print("都会被执行")"""

"""a,b = 1,8
a,b = b,a
print(a,b)"""

"""l1 = ["name","age"]
l2 = ['hacker',12]
ret = [i for i in zip(l1,l2)]
print(ret)"""

"""a = 'i am a 1'
import re
print(re.sub(r'\d+','100',a))"""

"""update student set gender=0 hometown='bej' where id=5"""

"""a = '你好'.encode()
b = b'hello'
print(type(a),type(b))"""

"""a = [1,2]
b = [3,4]
a.extend(b)
print(a)
print(a+b)"""

"""l = [2,5,99,22,8888,777]
l2 = []
for i in range(len(l)):
    k = min(l)
    l2.append(k)
    l.remove(k)
print(l2)"""

"""l1 = ["name","age"]
l2 = ['hacker',12]
l3 = zip(l1,l2)
d = dict(l3)
print(d)"""

"""a = '%.03f'%1.3335
print(a)
b = 1/3
print(round(b,10))"""

"""def fn(k,v,dic={}):
    dic[k]=v
    print(dic)
fn("name","oy")
fn("age",18)
fn("score",100000,{})"""

"""d = {"name":"dayang","age":18}
#d.pop("name")
del d["age"]
print(d)"""

"""A =zip(("a","b"),(1,2))
A1 = range(3)
A2 = dict(A)
A3 = [A2[s] for s in A2]
print(A)
print(A2)
print(A3)
d = dict([['a',1],['b',2]])
print(d)
d2 = dict([('a',1),('b',3)])
print(d2)"""

"""print(bool(0))"""

"""l = [True,False]
print(all(l))
print(any(l))"""

"""import copy
l = [1,2,[11,22]]

a = copy.deepcopy(l)
b = copy.copy(l)
l[2][1] = 999999999999999999999999999999999999
b.append(8888888888888)
a.append([11111,222222])
print(a)
print(l)
print(b)"""

"""a = (i for i in range(8))
print(type(a))
print(a)"""

"""def fun(k):
    print(1)
    yield k
    print("2")

fun(2222)
print(type(fun))"""

"""a = '        ddddd              '
a.strip(" ")
print(a)"""

"""l = [-1,-6,2,5,1,2,88,7]
l.sort()
print(l)
l2 = sorted(l,reverse=True)
print(l2)"""

"""l = [2,1,5,3,-1,-8,-3]
l.sort(key=lambda x:(x<0,abs(x)))
print(l)"""

"""l = [{"nane":"ls","age":23},{"nane":"xs","age":13},{"nane":"zs","age":123},{"nane":"ds","age":323}]
a = sorted(l,key=lambda x:x["age"])
print(a)
b = sorted(l,key=lambda x: x["nane"])
print(b)"""

"""l = [("zs",12),("ds",18),("ks",1)]
a = sorted(l,key=lambda x:x[0])
print(a)
b = sorted(l,key=lambda x:x[1])
print(b)"""

"""dic1 = {"name":"oy","sex":"man","city":"guiyang"}
l = zip(dic1.keys(),dic1.values())
l1 = [i for i in l]
l2 = sorted(l1,key=lambda x:x[0])
print(l2)
d1 = {i[0]:i[1] for i in l2}
print(d1)"""

"""dic1 = {"name":"oy","sex":"man","city":"guiyang"}
print(dic1.items())
a = sorted(dic1.items(),key=lambda x:x[0])
print(a)
print({i[0]:i[1] for i in a})"""

"""import random
l = [i for i in range(10)]
g = (i for i in range(10))
d = {k:random.randint(1,10) for k in ['a','b','c','d']}
print(l,type(l))
print(g,type(g))
print(d,type(d))"""

"""l = ["a",'bd','dddd','k','ddddddddddddddddddddddddddddd','cccccccccc']
a = sorted(l,key=lambda x:len(x))
print(a)"""

"""import re
s = "info:xiaozhang 22 shangdong 100"
s = re.split(r' |:',s)
print(s)"""

"""import re
email_list = ['aa163.com','bb163.comge','ccqq.com']
for i in email_list:
    k = re.findall(r'[\w]{2,9}163\.com$',i)
    print(k)"""

"""def get_sum(k):
    if k==0:
        ret=k
    else:
        ret = k + get_sum(k-1)
    return ret
r = get_sum(100)
print(r)"""

"""d = {'name':'hacker','age':23}
import json
j = json.dumps(d)
print(type(j),j)
d1 = json.loads(j)
print(type(d1),d1)"""

"""s = 'li li li li bai bai'
print(s.count('li'))"""

"""s = 'lllllllllllllliiiiiiiiiiiiiiiikkkkkkkkk'
print(s.upper())
print(s.lower())"""

"""s = 'hello world i am coming'
print(s.replace(' ',''))
print(''.join(s.split(' ')))"""

"""print(int(1.4),int('1.4'))"""

"""s = 'aaaaaaaaaaaaahttps://hao.360.com/?a1004aaaaaaaaaaaaaaaaaaaaaaaaahttps://hao.360.com/?a1004sssssssssssss'
import re
print(re.findall(r'https://.*?1004',s)[1])"""

"""import re
s = '你好 HELLO 世界'
pattren = re.compile(r'[\u4e00-\u9fa5]+')
print(pattren.findall(s))"""

"""l = [1,2,3]
ll = [3,4,5]
print(set(l).intersection(set(ll)))
print([i for i in l if i in ll])
print(set(l).difference(set(ll)))
print(list(set(l).union(set(ll))))"""

"""import random
print(random.choice(range(100)))"""

"""a = ["这个"," ","nage"]
print(list(map(lambda x:"填充" if x==" " else x ,a)))"""

"""import pandas
ret = pandas.read_excel('C:\\Users\\OY\\Desktop\\学习路线图.xlsx')
print(ret)"""

