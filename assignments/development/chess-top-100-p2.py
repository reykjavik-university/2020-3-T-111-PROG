# The following constants indicate the position of the respective
# fields in the tuple stored as the value for the key in the players dictionary
RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file(filename):
    ''' Open the given file name and returns the corresponding file stream, or None if the file cannot be opened '''
    try:
        file_stream = open(filename, 'r')
        return file_stream
    except FileNotFoundError:
        return None    

def create_players_dict(file_stream):
    ''' Reads the given file stream and returns a dictionary in which
        the name of a chess player is the key, the value is a tuple: (rank, country, rating, b-year)
    '''
    the_dict = {}
    for line in file_stream:	# process each line
        rank, name, country, rating, byear = line.split(';')
        # The name is one field separated by ","
        lastname, firstname = name.split(",")
        # Strip leading spaces
        firstname = firstname.strip()
        lastname = lastname.strip()
        country = country.strip()

        key = "{} {}".format(firstname, lastname)
        value_tuple = (int(rank), country, int(rating), int(byear))
        the_dict[key] = value_tuple
    return the_dict

def create_dict_with_key(dict_players, attribute_key):
    ''' Uses a players dictionary to create a dictionary
        in which an attribute in the values of dict_players are keys and a list of player names are values
    '''
    the_dict = {}
    for chess_player, chess_player_data in dict_players.items():
        key = chess_player_data[attribute_key]
        if key in the_dict:
            name_list = the_dict[key]
            name_list.append(chess_player)
        else:
            the_dict[key] = [chess_player]
    
    return the_dict


def get_average_rating(players, dict_players):
    ''' Returns the average ratings for the given players'''
    ratings = [ dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(the_dict, dict_players):
    ''' Prints information sorted on the key of the_dict '''
    sorted_dict = sorted(the_dict.items())
    for key, players in sorted_dict:
        average_rating = get_average_rating(players, dict_players)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))


def print_header(header_str):
    print(header_str)
    dashes = '-' * len(header_str)
    print(dashes)


# The main program starts here
filename = input("Enter filename: ")
file_stream = open_file(filename)
if file_stream:
    dict_players = create_players_dict(file_stream)
    dict_countries = create_dict_with_key(dict_players, COUNTRY)
    dict_years = create_dict_with_key(dict_players, BYEAR)
    print_header("Players by country:")
    print_sorted(dict_countries, dict_players)
    print()
    print_header("Players by birth year:")
    print_sorted(dict_years, dict_players)