def rotate_text_clockwise(text):
    """ Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings """
    lines = text.splitlines()
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
    rotated_text = ""
    for character_index in range(max_length):
        for line in reversed(lines):
            if len(line) > character_index:
                character_to_add = line[character_index]
            else:
                character_to_add = " "
            rotated_text += character_to_add
        rotated_text += "\n"
    return rotated_text.rstrip("\n")


def determine_clearance(text, max_width):
    min_clearance_left = max_width
    min_clearance_right = max_width
    for line in text.splitlines():
        clearance_left = len(line) - len(line.lstrip(" "))
        min_clearance_left = min(clearance_left, min_clearance_left)
        clearance_right = max_width - len(line)
        min_clearance_right = min(clearance_right, min_clearance_right)
    return min_clearance_left, min_clearance_right


def change_indentation(text, spaces):
    """Adds or removes leading spaces to/from every line in the supplied string.

    A negative number of spaces instructs the function to remove spaces.
    A positive number of spaces instructs the function to add spaces.
    This function will automatically adjust the number of spaces to ensure that no line exceeds 80 characters.
    For example, if there's a line that's 78 characters long, and spaces = 4, then the function will only add
    2 spaces to each line.
    Similarily, it will not remove more spaces than it can. If one line has only 2 leading spaces and spaces = -4,
    then the function will remove exactly 2 spaces from each line."""

    # Figure out how much clearance we have on the left and right
    MAX_WIDTH = 80
    clearance_left, clearance_right = determine_clearance(text, MAX_WIDTH)

    # Adjust the number of spaces added/removed, if needed, to ensure that the resulting string:
    # - stays within the maximum width when adding spaces
    # - doesn't remove any leading non-whitespace characters
    if spaces > 0:
        spaces = min(spaces, clearance_right)
    elif spaces < 0:
        spaces = max(spaces, clearance_left * -1)

    # Is there anything for us to do?
    if spaces == 0:
        return text  # Nope

    # Adjust indentation
    result = ""
    for line in text.splitlines():
        if spaces > 0:
            result += " " * spaces + line + "\n"
        elif spaces < 0:
            result += line[abs(spaces) :] + "\n"

    # Remove the last newline character which got appended in the last iteration of the loop
    result = result.rstrip("\n")
    return result


piece = """X
XXX"""
indentation = 0
action = ""
while action != "q":
    print(change_indentation(piece, indentation))
    action = input("(r)ight, (l)eft, (t)urn, (q)uit: ").lower()
    if action == "r":
        indentation += 1
    elif action == "l":
        indentation -= 1
    elif action == "t":
        piece = rotate_text_clockwise(piece)
