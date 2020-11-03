from island import Island

class Animal():
    NOT_FOUND = 0
    breed_time = 10  # class varible. Not really used because the subclasses have their own breed times

    @classmethod
    def set_breed_time(cls, breed_time):     # A class method for setting the starting breed time for all the instances
        cls.breed_time = breed_time 

    def __init__(self, island, x=0, y=0, name='A'):
        '''Initializes the animal and its position'''
        # Variables starting with a single underscore are 'protected', accessible in subclasses
        # Variables starting with two underscores are 'private', not accessible outside the class
        self._island = island  
        self._x = x    # value on x-axis, 
        self._y = y    # value on y-axis, 
        self.__name = name
        self._moved = False    # indicating that the instance has not moved during the current clock tick
        self._breed_clock = self.breed_time  

    def __str__(self):
        return self.__name

    def _check_grid_for_neighbor(self, type_looking_for):
        '''Look in the 8 directions from the animals' location and returns the first
        neighbor location that presently has an object of the specified type. 
        Returns NOT_FOUND if no such location exists'''
        offset = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
        result = Animal.NOT_FOUND

        for dx, dy in offset:
            x = self._x + dx
            y = self._y + dy
            # We either find a specific animal or empy cell
            if type(self._island.animal(x,y)) == type_looking_for:
                result = (x,y)
                break  # Quit immediately if a location is found 
        return result

    def clock_tick(self):  
        self._breed_clock -= 1

    def position(self):
        return (self._x, self._y)
    
    def clear_move(self):
        self._moved = False

    def move(self):
        '''Moves to an open neighboring position, but only if it has not already moved during the clock tick.'''
        if not self._moved: 
            location = self._check_grid_for_neighbor(type(Island.UNOCCUPIED))
            if location != Animal.NOT_FOUND:
                self._island.remove(self)      # Remove the animal from the island
                self._x, self._y = location    # x and y coordinates
                self._island.register(self)    # Register the animal on the island
                self._moved = True             # Now it has moved
        
    def breed(self):
        '''Breed a new Animal.  If there is room in one of the neigboring locations,
        place the new animal there.'''
        if self._breed_clock <= 0:
            location = self._check_grid_for_neighbor(type(Island.UNOCCUPIED))
            if location != Animal.NOT_FOUND:
                the_class = self.__class__
                # Reset the breed clock
                self._breed_clock = the_class.breed_time    # breed_time is a class variable
                # Create an instance of a new animal
                new_animal = the_class(self._island, x=location[0], y=location[1])
                self._island.register(new_animal)
