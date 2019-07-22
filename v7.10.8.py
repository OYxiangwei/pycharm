l = [('ll',12),('xx',18),('KK',222)]
def by_name(t):
    t = sorted(t[0],key=str.lower)
    return t
def by_score(t):
    t = sorted(range(t[1]),key=abs)
    return t
l2 = sorted(l,key=by_score)
print(l2)