class Order():

    def __init__(self, item, price):
        self.__item = item
        self.__price = price
    
    def __str__(self):
        return "Item: {}, price: {}".format(self.item(), self.price())

    def __gt__(self, other):
        return self.price() > other.price()
    
    def __add__(self, other):
        new_item = self.item() + "+" + other.item()
        return Order(new_item, self.price() + other.price())

    def item(self):
        return self.__item

    def price(self):
        return self.__price