class Ticket():
    def __init__(self,weekend=False,child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_price(self,num):
        return self.exp * self.inc * self.discount * num

adult = Ticket()
child = Ticket(weekend=True,child=True)
print("two adult an one child price{0}".format(adult.cal_price(1)+child.cal_price(1)))