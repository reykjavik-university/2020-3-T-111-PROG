"""A program that prepares to calculate final grades of students in this course.

Takes as input a .csv file exported from the gradebook on Mímir.
We need to extract information for every student on how many points they scored
in individual quizzes, assignments, projects and exams,
as well as the maximum available points for each.

Since not all of those have been performed in Mímir already,
it is unknown at this time in which order they will appear in the file.
So this program identifies the columns dynamically
(after the semester is over, it will be possible to simplify this program
by providing this mapping as hard-coded constants).

Next, it extracts information from the file, about the maximum available points for each coursework,
and prints it out (nicely formatted), to show an example of what can be done with the results.
"""

import csv


# https://stackoverflow.com/questions/6088581/what-are-python-best-practices-for-dictionary-dict-key-constants
FIRST_NAME = "first name"
LAST_NAME = "last name"
EMAIL = "email"
SECTION = "section"

QUIZZES = "quiz"
ASSIGNMENTS = "assignment"
EXTRA_ASSIGNMENTS = "extra assignment"
PROJECTS = "project"
MIDTERMS = "midterm"
FINAL_EXAM = "final exam"

HEADER_PREFIXES = {
    FIRST_NAME: "First Name",
    LAST_NAME: "Last Name",
    EMAIL: "Email",
    SECTION: "Section",
    QUIZZES: "Quiz",
    ASSIGNMENTS: "Assignment",
    PROJECTS: "Project",
    MIDTERMS: "Midterm",
    FINAL_EXAM: "Final exam"
}



def main():
    filename = input("Enter filename: ")
    grades = read_grades_from_file(filename)
    if grades:
        index_dict = identify_columns(headers_line=grades[0])
        points_possible = get_points_possible(subheaders_line=grades[1], columns=index_dict)
        display_max_points(index_dict, points_possible, headers_line=grades[0])


def read_grades_from_file(filename:str) -> list:
    """Parses the file into a list of lists, one for each line of the file."""
    try:
        with open(filename, encoding='utf-8') as grade_file:
            return list(csv.reader(grade_file))

    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None


def identify_columns(headers_line:list) -> dict:
    """Figures out what the indices of various headers are.

    Args:
      headers_line:
        The first line of the gradebook, which contains the column headers.
        Will not be modified.
    
    Returns:
        A dictionary with the indices of all relevant headers.
        For example:

        {
            FIRST_NAME: 0,
            LAST_NAME: 1,
            EMAIL: 2,
            SECTION: 3,
            QUIZZES: [4, 6, 8, 12, 16, 20, 24, 28],
            ASSIGNMENTS: [5, 9, 14, 17, 19, 26, 29, 32, 34],
            EXTRA_ASSIGNMENTS: [7, 10, 13, 18, 21, 25, 30],
            PROJECTS: [11, 15, 22, 27, 33],
            MIDTERMS: [23, 31],
            FINAL_EXAM: 35,
        }

        The intended use of this dictionary is demonstrated by the following examples:
        >>> columns = identify_columns(gradebook[0])
        Given a line from the gradebook for a particular student:

        1. The name of the student is found as:
        >>> name = f"{line[columns[FIRST_NAME]]} {line[columns[LAST_NAME]]}"

        2. Index of grade from final exam (which is unique):
        >>> final_exam_score = line[columns[FINAL_EXAM]]

        3. Index of grades from other categories, such as projects:
        >>> project_scores = [line[column] for column in columns[PROJECTS]]
    """

    columns = {}
    for category in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
        columns[category] = []

    for index, header in enumerate(headers_line):
        category = determine_category(header)
        if category in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
            columns[category].append(index)
        elif category in [FIRST_NAME, LAST_NAME, EMAIL, SECTION, FINAL_EXAM]:
            columns[category] = index

    return columns


def determine_category(header:str) -> str:
    """Determines which category the given header belongs to."""

    # Special care must be taken to distinguish between the normal assignments and the extra assignments.
    # The header for assignment 1 begins with "Assignment 1:".
    # The header for assignment 1+ begins with "Assignment 1+:"
    # They share the prefix "Assignment 1"
    # so checking the header for the prefix "Assignment" is not enough to distinguish between these two categories.

    for category in HEADER_PREFIXES:
        if header.startswith(HEADER_PREFIXES[category]):
            if category == ASSIGNMENTS and "+:" in header:
                return EXTRA_ASSIGNMENTS
            return category

    return "Unknown"


def get_points_possible(subheaders_line:list, columns:dict) -> dict:
    """Reads maximum available points for each grade from the file.

    Args:
      subheaders_line:
        The second line of the gradebook,
        which contains the maximum available points for each coursework.
        Will not be modified.
      columns:
        A dictionary with the indices of all relevant headers.
        Will not be modified.
    
    Returns:
        A dictionary with the maximum points that can be scored for each coursework.
        Intended to be used for comparison with grades of an individual student,
        as demonstrated by the following:

        >>> points_possible = get_points_possible(gradebook[1], columns)
        >>> max_points = points_possible[category]
        >>> points = [float(student_line[column]) for column in columns[category]]
        >>> assert len(points) == len(max_points)
        >>> assert all([0 <= score <= maximum > 0 for score, maximum in zip(points, max_points))
        >>> grades = [score / maximum for score, maximum in zip(points, max_points)]
    """

    assert subheaders_line[0] == "Points Possible"
    points_possible = {}
    for key in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
        points_possible[key] = [float(subheaders_line[column]) for column in columns[key]]
    points_possible[FINAL_EXAM] = float(subheaders_line[columns[FINAL_EXAM]]) if FINAL_EXAM in columns else 1
    return points_possible


def display_max_points(indices:dict, points_possible:dict, headers_line:list) -> None:
    """Prints out the maximum available points for each coursework along with the corresponding headers.

    Args:
      indices:
        A dictionary with the indices of all relevant headers.
        Will not be modified.
      points_possible:
        A dictionary with the maximum points that can be scored for each coursework.
        Will not be modified.
      headers_line:
        The first line of the gradebook, which contains the column headers.
        Will not be modified.
    """

    DECIMAL_PLACES = 1
    INDENT_ALIGN = 5 + DECIMAL_PLACES

    print()

    headers = {
        QUIZZES: "Quizzes:",
        ASSIGNMENTS: "Assignments:",
        EXTRA_ASSIGNMENTS: "Extra assignments:",
        PROJECTS: "Projects:",
        MIDTERMS: "Midterms:"
    }

    for category in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
        print(headers[category])
        index_list = indices[category]
        max_points_list = points_possible[category]
        for i in range(len(index_list)):
            max_points = max_points_list[i]
            index = index_list[i]
            coursework = headers_line[index]
            print(f"{max_points:>{INDENT_ALIGN}.{DECIMAL_PLACES}f} points possible for {coursework}")
    
    if FINAL_EXAM in indices:
        max_points = points_possible[FINAL_EXAM]
        index = indices[FINAL_EXAM]
        label = headers_line[index]
        print(f"{max_points} points possible for {label}")
    else:
        print("The number of possible points on the final exam is not available yet.")


main()
