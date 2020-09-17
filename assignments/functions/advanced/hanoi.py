# Use recursion to solve the Tower of Hanoi puzzle
# The objective is to get n discs, stacked on the first pillar, over to the third pillar.
# To do so:
# - we first get the n-1 discs over to the second pillar (via recursion)
# - then we can move the one remaining (and largest) disc from the first pillar to the third pillar
# - finally we get the n-1 discs from the second pillar to the third pillar (via recursion)

def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    seen_so_far = 0
    for index, element in enumerate(sequence):
        if element == element_to_find:
            seen_so_far += 1
            if seen_so_far == occurrence:
                return index
    return -1


def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    removed_element = sequence[index_to_remove]
    updated_sequence = sequence[:index_to_remove] + sequence[index_to_remove + 1:]
    return updated_sequence, removed_element


def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    return sequence[:index] + element + sequence[index:]


def move_one(from_pillar, to_pillar, state):
    """ Moves the topmost disc from one pillar to another and returns the updated state representation. """
    where_to_remove = find_index_of_nth_occurrence(sequence=state, element_to_find="|", occurrence=from_pillar) - 1
    state, disc_to_move = remove_at(sequence=state, index_to_remove=where_to_remove)
    where_to_insert = find_index_of_nth_occurrence(sequence=state, element_to_find="|", occurrence=to_pillar)
    state = insert_at(sequence=state, index=where_to_insert, element=disc_to_move)
    return state


def move_many(how_many, from_pillar, to_pillar, state):
    """ Moves the specified number of discs from one pillar to another and returns the updated state representation. 
    
    Prints the state for every move made.
    """
    if how_many > 0:
        auxiliary_pillar = 6 - from_pillar - to_pillar
        state = move_many(how_many - 1, from_pillar, auxiliary_pillar, state)
        state = move_one(from_pillar, to_pillar, state)
        print(state)
        state = move_many(how_many - 1, auxiliary_pillar, to_pillar, state)
    return state


number_of_discs = int(input("How many discs are on the left-most pillar? "))
initial_state = ""
for disc in range(number_of_discs, 0, -1):
    initial_state += str(disc)
initial_state += "|||"
print(initial_state)
move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)
