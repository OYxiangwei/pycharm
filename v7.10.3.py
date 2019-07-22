class MyError(Exception):
    def __init__(self,stri):
        self.stri = stri

    def process(self):
        if len(self.stri) < 5:
            print("字符串的长度必须大于5")
        else:
            print("聪明")
try:
    m1 = MyError('eeee')
    m1.process()
except Exception as e:
    print(e)