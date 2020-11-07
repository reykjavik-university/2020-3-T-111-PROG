# Open file
# Read file contents into a dictionary
# Print information from dictionary
# Print name of person who has visitied most contries

def open_file(file_name):
    ''' Opens the given file name and returns the corrsponding stream '''
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

def create_flyers_dict(file_stream):
    ''' Creates a dictionary from the given file stream.
        The name is the key, the set of countries is the value '''
    flyers = {}
    for line in file_stream:
        name, country = line.split()
        if name not in flyers:
            flyers[name] = {country}
        else:
            flyers[name].add(country)
    return flyers

def print_dict(flyers):
    ''' Prints info from flyers ordered by key.
        The values is also printed ordered '''
    for name in sorted(flyers.keys()):
        print("{}:".format(name))
        for country in sorted(flyers[name]):
            print("\t{}".format(country))

def visited_most_countries(flyers):
    countries_count = 0
    max_flyer = ''
    for name, countries in flyers.items():
        if len(countries) > countries_count:
            countries_count = len(countries)
            max_flyer = name
    return max_flyer, countries_count

def print_most_visited(name, count):
    print()
    print("{} has been to {} countries".format(name, count))

# Main program starts here
file_name = "flights.txt"
file_stream = open_file(file_name)
flyers = create_flyers_dict(file_stream)
print_dict(flyers)
name, count = visited_most_countries(flyers)
print_most_visited(name, count)