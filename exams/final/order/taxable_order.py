from order import Order

class TaxableOrder(Order):
    def __init__(self, item, price, tax_ratio):
        super().__init__(item, price)
        self.__tax_ratio = tax_ratio
    
    def price(self):
        return round(super().price() * (1 + self.__tax_ratio), 1)
    