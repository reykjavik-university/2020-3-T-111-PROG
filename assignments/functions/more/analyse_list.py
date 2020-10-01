
def get_data():
    '''Returns a list of positive integers input by a user. 
        An empty list is returned if the input contains non-integers or integers < 0'''
    a_list = input('Enter integers separated with commas: ').split(',')
    try:
        int_list = [ int(elem) for elem in a_list]
        for num in int_list:
            if num <= 0:
                return [] 
        return int_list
    except ValueError:
        return []

def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def stats_from_list(int_list):
    ''' Returns statistics from the given list: min, max and average '''
    max_int = max(int_list)
    min_int = min(int_list)
    average = sum(int_list) / len(int_list)
    return (min_int, max_int, average)

def print_lists(input_list, sorted_list, prime_list):
    ''' Prints the given lists '''
    print('Input list:', input_list)
    print('Sorted list: ', sorted_list)
    print('Prime list: ', prime_list)

def print_stats(min_int, max_int, average):
    ''' Prints the statistics '''
    print('Min: {:d}, Max: {:d}, Average: {:.2f}'.format(min_int, max_int, average))

def unique_elements(a_list):
    ''' Returns a new list containing the unique elements in a_list '''
    result = []
    for elem in a_list:
        if not elem in result:
            result.append(elem)
    return result

# Main program start here
input_list = get_data()
if input_list:
    sorted_list = sorted(input_list)
    prime_list = unique_elements([ elem for elem in sorted_list if is_prime(elem)])
    print_lists(input_list, sorted_list, prime_list)
    min_int, max_int, average = stats_from_list(input_list)
    print_stats(min_int, max_int, average) 
else:
    print('Incorrect input!')