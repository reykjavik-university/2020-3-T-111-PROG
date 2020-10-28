# A simulated cash register that tracks the item count and the total amount due

class CashRegister:

    def __init__(self, tax_rate):
        '''Constructs a cash register with cleared item count and totals.
        param tax_rate is the tax rate to be used in the register.'''
        self.clear()
        self.__tax_rate = tax_rate
    
    def add_item(self, price, taxable):
        '''Adds an item with the give price to the register.
        param taxable is True if the item is taxable.'''
        self.__item_count += 1
        self.__total_price += price
        if taxable:
            self.__total_taxable += price
    
    def get_total(self):
        '''Gets the total price (excluding the tax) of all items in the register.'''
        return self.__total_price 

    def get_total_with_tax(self):
        '''Gets the total price, including the tax, of all items in the register.'''
        return self.__total_price + self.__total_taxable * self.__tax_rate / 100.0

    def get_count(self):
        '''Returns the number of items in the register'''
        return self.__item_count
    
    def clear(self):
        '''Clears the item count and the totals'''
        self.__item_count = 0
        self.__total_price = 0.0
        self.__total_taxable = 0.0
    
    def __str__(self):
        return "Items: {}, total price: {:.2f}, including tax: {:.2f}".format(self.__item_count, self.__total_price, self.get_total_with_tax())
