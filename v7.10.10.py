goods = [{"name":'good1','price':100,'sales':300},
         {'name':'good2','price':200,'sales':200}]
def my_sort(arg):
    name = arg['name']
    price = arg['price']
    sales = arg['sales']
    data = price*0.3+sales*0.7
    return data
print(sorted(goods,key=my_sort))

d = sorted(goods,key=lambda x:x['price']*0.3+x['sales']*0.7)
print(d)