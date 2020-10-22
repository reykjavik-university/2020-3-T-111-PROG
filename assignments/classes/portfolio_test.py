from portfolio import *

stock1 = Stock('IBM', 100)
print(stock1)
stock2 = Stock('GOOG', 200)
stock3 = Stock('AMZN', 500)

portfolio = Portfolio()
portfolio.add(stock1)
portfolio.add(stock2)
portfolio.add(stock3)
print()
print(portfolio)
