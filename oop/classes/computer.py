class Computer:
    def __init__(self):
        self.__privatePrice = 900
        self.price = 1000

    def sell(self):
        print("Selling price: {}".format(self.__privatePrice))

    def setPrivatePrice(self, price):
        self.__privatePrice = price

    def getPrivatePrice(self):
        return self.__privatePrice


c = Computer()
print(c.price)
c.setPrivatePrice(800)
print(c.getPrivatePrice())
c.sell()
