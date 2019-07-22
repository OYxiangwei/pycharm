ls = ['ssss','dddd','kkk','yy']
print(list(map(lambda x:x.lower().capitalize(),ls)))

rg = range(1000)
k = filter(lambda x:str(x)[0] == str(x)[len(str(x))-1],rg)
print(list(k))