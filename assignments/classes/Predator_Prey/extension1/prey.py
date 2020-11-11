from animal import Animal

class Prey(Animal):
        
    def __init__(self, island, x=0, y=0, name='O'):
        super().__init__(island, x, y, name) # or Animal.__init__(self, island, x, y, name)
    