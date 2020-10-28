class Grid(object):
    CHAR_EMPTY = 'o'
    CHAR_POS = 'x'
    DEFAULT_ROW = 1
    DEFAULT_COL = 1
    
    def __init__(self, rows=1, cols=1):
        self.rows = rows
        self.columns = cols
        self.current_row = Grid.DEFAULT_ROW
        self.current_col = Grid.DEFAULT_COL

    def __str__(self):
        result_str = ''
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.current_row, self.current_col) == (i+1,j+1):
                    result_str += Grid.CHAR_POS
                else:
                    result_str += Grid.CHAR_EMPTY
            result_str += '\n'
        return result_str 


    def move_left(self):
        if self.current_col > 1:
            self.current_col -= 1
        else:
            self.current_col = self.columns
        
    def move_right(self):
        if self.current_col < self.columns:
            self.current_col += 1
        else:
            self.current_col = 1

    def move_up(self):
        if self.current_row > 1:
            self.current_row -= 1
        else:
            self.current_row = self.rows
    
    def move_down(self):
        if self.current_row < self.rows:
            self.current_row += 1
        else:
            self.current_row = 1

    def current_pos(self):
        return (self.current_row, self.current_col) 

