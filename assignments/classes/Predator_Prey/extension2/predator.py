from animal import Animal
from prey import Prey

class Predator(Animal):
    starve_time = 5 # class variable

    @classmethod
    def set_starve_time(cls, starve_time):     # A class method for setting the starting starve time for all the instances
        cls.starve_time = starve_time 

    def __init__(self, island, x=0, y=0, name='X'):
        super().__init__(island, x, y, name) # or Animal.__init__(self, island, x, y, name)
        self.__starve_clock = self.starve_time 
    
    def eat(self):
        '''Predator looks for a Prey.  If found, removes Prey, moves to that location,
        updates the starve clock, but only if it has not already moved during the clock tick.'''
        if not self._moved:  
            location = self._check_grid_for_neighbor(Prey)
            if location != Animal.NOT_FOUND:
                self._island.remove(self._island.animal(location[0], location[1]))
                self._island.remove(self)
                self._x, self._y = location
                self._island.register(self)
                self._moved = True
                self.__starve_clock = self.starve_time

    def clock_tick(self):
        super().clock_tick()
        self.__starve_clock -= 1
        if self.__starve_clock <= 0:      # A Predator can die from starvation
            self._island.remove(self)