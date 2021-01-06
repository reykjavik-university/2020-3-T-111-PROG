DIM = 8 # The dimension of a chess board
FEN_SEPARATOR = '/'
EMPTY = ' '

# Starting chess position: 
# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
# After 1. e4 c5 2. Nf3 Nc6:
# r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R

def display_board(board):
    '''Displays the chess board'''
    count = DIM
    for rank in board:
        print(count, rank)
        count -= 1
    print('  abcdefgh')

def expand_fen_rank(rank_str):
    '''Returns a DIM length string corresponding to the given rank_str.
    Each position in the rank_str either contains an alphabetical character denoting a piece on the corresponding square
    or a digit which signifies number of empty squares.
    Each position in the returned string indicates a piece or an empty square'''
    result_str = ''
    for ch in rank_str:
        if ch.isdigit():    # ch denotes number of empty square
            num = int(ch)
            substring = EMPTY*num   # string containing num EMPTY characters
            result_str += substring
        else:   # ch denotes a piece
            result_str += ch
    
    return result_str

def get_board_position(fen_position_str):
    '''Returns the chess board position indicated by the fen_position_str.
    The board is a list of DIM elements, each element is a string of DIM characters'''

    board = []
    # fen_ranks is a list of DIM strings.  Each string denotes pieces on a rank on the board.
    fen_ranks = fen_position_str.split(FEN_SEPARATOR)

    for rank in fen_ranks:
        expanded_str = expand_fen_rank(rank)
        board.append(expanded_str)
    
    return board

def get_board_errors(board):
    '''Returns a list of ranks that contain errors for the given board position.'''
    error_list = []
    for i in range(DIM):
        if len(board[i]) != DIM:
            error_list.append(DIM-i)

    return error_list

# Main program starts here
fen_position_str = input("Enter a FEN string: ")
board = get_board_position(fen_position_str)
error_list = get_board_errors(board)
if error_list:
    print("Errors in ranks: {}".format(error_list))
else:
    display_board(board)