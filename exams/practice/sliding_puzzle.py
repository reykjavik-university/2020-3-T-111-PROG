# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()


def get_current_pos(board, number):
    ''' Returns the two-dimensional position (i,j) corresponding to the given number '''
    for i in range(DIM):
        for j in range(DIM):
            if board[i][j] == number:
                return (i, j)
    
def get_new_position(board, current_pos):
    ''' Returns the two-dimensional position from which the current position can move to.
        Returns None if a move cannot be made '''
    i, j = current_pos
    if j > 0 and board[i][j-1] == EMPTYSLOT:    # moving left
        return (i, j-1)
    if j < DIM-1 and board[i][j+1] == EMPTYSLOT:# moving right    
        return (i, j+1)
    if i > 0 and board[i-1][j] == EMPTYSLOT:    # moving down
        return (i-1, j)
    if i < DIM-1 and board[i+1][j] == EMPTYSLOT:# moving up
        return (i+1, j)
    return None

def make_move(board, number): 
    ''' Makes a single move respresented by the given number on the given board '''
    current_pos = get_current_pos(board, number)
    new_position = get_new_position(board, current_pos)
    if new_position != None:
        update_board(board, current_pos, new_position, number)

def update_board(board, current_pos, new_position, number):
    ''' Updates the board setting new_position with the given number and curren_position with EMPTYSLOT '''
    current_i, current_j = current_pos
    new_pos_i, new_pos_j = new_position
    board[current_i][current_j] = EMPTYSLOT
    board[new_pos_i][new_pos_j] = number

def main():
    board = initialize_board()
    number = -1
    while number != QUIT:
        display(board)
        number = int(input())
        make_move(board, number)

main()