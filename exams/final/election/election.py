def get_candidate_votes():
    '''Returns a tuple consising of a name of a candidate and votes given to him/her.
    Either or both of the elements of the tuple can have the value None indicating an invalid input.'''

    candidate, votes = None, None

    input_list = input("Candidate and votes: ").split()
    if len(input_list) > 0:
        candidate = input_list[0].lower()
        if len(input_list) > 1:
            try:
                votes = int(input_list[1])
            except ValueError:
                pass
    
    return candidate, votes
    
def add_results(result_dict, candidate, votes):
    '''Adds the votes to the given to candidate in the given dictionar'''
    if candidate in result_dict:
        result_dict[candidate] += votes
    else:
        result_dict[candidate] = votes

def get_total_votes(result_dict):
    '''Returns the total number of votes for the given result dictionary'''
    total = 0
    for candidate in result_dict:
        total += result_dict[candidate]
    
    return total

    # Simpler solution
    # return sum(result_dict.values())

def print_results(result_dict):
    '''Prints the current results of the election in ascending order candidate names'''
    for candidate in sorted(result_dict):
        print("{}: {}".format(candidate, result_dict[candidate]))

# Main    
election_dict = {}
candidate = ''

while candidate is not None:
    candidate, votes = get_candidate_votes()
    if candidate is not None:
        if votes is not None:
            add_results(election_dict, candidate, votes)
        else:
            print("Invalid no. of votes!")

print_results(election_dict)
print("Total no. of votes: {}".format(get_total_votes(election_dict)))
