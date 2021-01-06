HIGH_TOTAL_SCORE = 1000     # Total score should in practise never reach this
LOWEST_SCORE_TRIGGER = 10   # Minimum number of players to trigger lowest score calculation

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def add_score_to_dict(scores_dict, name, score):
    '''Adds score to the list of scores for key name in scores_dict '''
    if name in scores_dict:
        scores_dict[name].append(score)
    else:
        scores_dict[name] = [score]
    
def populate_dict(score_dict, file_stream):
    ''' Populates score_dict with scores from file_stream 
        Each line in file_stream consists of 
        <first_name last_name score>'''
    
    for line in file_stream:
        first_name, last_name, score = line.split()
        score = int(score)
        full_name = first_name + " " + last_name
        add_score_to_dict(score_dict, full_name, score)

def print_dict(score_dict):
    for name, score_list in score_dict.items():
        print('Player: {:<20s}Scores: '.format(name), end='')
        print(" ".join([str(x) for x in score_list]))
        # for score in score_list:
        #     print(score, end=' ')
        # print()

def find_lowest_total_score(score_dict):
    '''Returns a tuple (name, total_score) for the player with the lowest total score'''
    lowest_score = HIGH_TOTAL_SCORE
    for name, score_list in score_dict.items():
        total_score = sum(score_list)
        if total_score < lowest_score:
            lowest_tuple = (name, total_score)
            lowest_score = total_score
    return lowest_tuple

def print_lowest_total(lowest_tuple):
    '''Prints the name and the score in lowest_tuple = (name, score)'''
    (name, score) = lowest_tuple
    print('{} has the lowest total score: {}'.format(name, score))

def main():
    score_file = input("Enter file name: ")
    file_stream = open_file(score_file)
    if file_stream:
        score_dict = {}
        populate_dict(score_dict, file_stream)
        file_stream.close()
        print_dict(score_dict)
        if len(score_dict.keys()) >= LOWEST_SCORE_TRIGGER: 
            lowest_tuple = find_lowest_total_score(score_dict)
            print_lowest_total(lowest_tuple)

main()