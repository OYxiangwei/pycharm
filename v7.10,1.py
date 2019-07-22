def jian(a,b):
    if a<b:
        raise BaseException("被减数不能小于减数")
    else:
        return a-b
try:
    ret = jian(3,2)
    print(ret)
except BaseException as e:
    print(e)