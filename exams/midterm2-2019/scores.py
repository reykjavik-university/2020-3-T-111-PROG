# This program computes a final score for a series of quiz scores: 
# the sum after dropping the lowest two scores

def read_scores():
    scores = input("Enter scores separated by space: ").strip().split()
    scores = [float(i) for i in scores]
    return scores

def remove_minimum(number_list):
    smallest_index = 0
    for i in range(1, len(number_list)):
        if number_list[i] < number_list[smallest_index]:
            smallest_index = i
    number_list.pop(smallest_index)
    # Mun einfaldari lausn
    #number_list.remove(min(number_list))

# Main program starts here
scores = read_scores()
if len(scores) > 1:
    remove_minimum(scores)
    remove_minimum(scores)
    print("Sum of scores (two lowest removed):", sum(scores))
else:
    print("At least two scores needed!")