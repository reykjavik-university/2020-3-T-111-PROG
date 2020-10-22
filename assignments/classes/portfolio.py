class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares
    
    def __str__(self):
        return "{}: {}".format(self.symbol, self.shares)

class Portfolio:
    def __init__(self):
        self.stocks = []
    
    def add(self, stock):
        self.stocks.append(stock)
    
    def __str__(self):
        return "\n".join([str(stock) for stock in self.stocks])