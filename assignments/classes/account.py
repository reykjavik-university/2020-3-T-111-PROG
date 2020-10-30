class Account:
    def __init__(self, balance):
        self._balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self._balance)


class SavingsAccount(Account):
    INTEREST_RATE = 0.05
    BONUS_RATE = 0.10

    def update_balance(self):
        self._balance = self._balance * (1 + self.INTEREST_RATE + self.BONUS_RATE) 


class DebitAccount(Account):
    INTEREST_RATE = 0.02

    def update_balance(self):
        self._balance = self._balance * (1 + self.INTEREST_RATE)
    