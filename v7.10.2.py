import os
def op(filename):
    try:
        f = open(filename)
    except Exception as e:
        print(e)
    else:
        print(f.read())
        f.close()
op('str_num.txt')