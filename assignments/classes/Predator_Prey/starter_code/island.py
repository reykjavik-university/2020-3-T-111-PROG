class Island():
    '''Island is an n-by-n grid where a special value indicates an UNOCCUPIED cell.'''
    UNOCCUPIED = 0
    OUTSIDE = -1
    
    def __init__(self, n):
        '''Initializes all cells in an n-by-n grid to UNOCCUPIED'''
        self.__grid_size = n
        self.__grid = []
        for _ in range(n):
            row = [Island.UNOCCUPIED]*n
            self.__grid.append(row)

    def __str__(self):
        '''Returns a string representation of the island. (x=0,y=0) is lower left corner.'''
        result_str = ''
        for y in range(self.__grid_size-1, -1, -1):   # print row size-1 first
            for x in range(self.__grid_size):
                if self.__grid[x][y] == Island.UNOCCUPIED:
                    result_str += "{:<s}".format('.  ')
                else:
                    result_str += "{:<s}".format(str(self.__grid[x][y]) + '  ')
            result_str += '\n'
        
        return result_str

    def inside(self, x, y):
        '''Returns True if the given coordinates are inside the island, else False'''
        return 0 <= x < self.__grid_size and 0 <= y < self.__grid_size

    def animal(self, x, y):
        '''Returns the animal at location (x,y)'''
        if self.inside(x,y):
            return self.__grid[x][y]
        else:
            return Island.OUTSIDE

    def size(self):
        return self.__grid_size

    def register(self, animal):
        '''Register animal in the island'''
        x,y = animal.position()     # a tuple (x,y)
        self.__grid[x][y] = animal 
    
    def remove(self, animal):
        '''Removes the animal from the island'''
        x,y = animal.position()     # a tuple (x,y)
        self.__grid[x][y] = Island.UNOCCUPIED
    
    def clear_all_moved_flags(self):
        '''Clear all the moved flags of all the instances on the island'''
        for x in range(self.__grid_size):   
            for y in range(self.__grid_size):
                animal = self.__grid[x][y]
                animal.clear_move()
