def shuffle(original_list: list, start_from_back: bool = False) -> list:
    """Returns a shuffled copy of the supplied list. The original list is not modified.

    Let n denote the length of the list. The shuffled order is then as follows:
    0, n-1, 1, n-2, 2 ... and so forth

    If start_from_back == True then the shuffled order is:
    n-1, 0, n-2, 1, n-3 ... and so forth
    """
    result = []
    length = len(original_list)
    for i in range(length):
        if i % 2 == 0:
            location = i // 2
        else:
            location = length - 1 - i // 2
        if start_from_back:
            location = location * (-1) - 1
        result.append(original_list[location])
    return result
