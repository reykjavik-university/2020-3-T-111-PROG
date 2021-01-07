DIM = 8 # The dimension of a chess board
FEN_SEPARATOR = '/'
EMPTY = ' '

def display_board(fen_string_list):
    '''Displays the chess board'''
    count = DIM
    for fen_string in fen_string_list:
        expanded_str = expand_fen_rank(fen_string)
        print(count, expanded_str)
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

def check_errors(fen_string_list):
    '''Returns a list of ranks that contain errors for the given list of fen strings.'''
    error_list = []
    for i, fen_string in enumerate(fen_string_list):
        expanded_str = expand_fen_rank(fen_string)
        if len(expanded_str) != DIM:
            error_list.append(DIM-i)
    return error_list
        

fen_string_list = input("Enter a FEN string: ").split(FEN_SEPARATOR)
errors = check_errors(fen_string_list)
if errors:
    print("Errors in ranks: {}".format(errors))
else:
    display_board(fen_string_list)