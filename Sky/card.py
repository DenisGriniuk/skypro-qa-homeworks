class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknow'

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.valiDate = date

    def pay(self, amount):
        print("с карты" , self.number, " списали", amount)

