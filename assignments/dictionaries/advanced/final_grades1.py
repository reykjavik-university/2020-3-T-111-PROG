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

Then the program prints out the identified indices (nicely formatted),
to show an example of what can be done with the results.
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
        display_index_dict(index_dict, headers_line=grades[0])

def read_grades_from_file(filename:str) -> list:
    '''Parses the file into a list of lists, one for each line of the file '''

    try:
        with open(filename, encoding='utf-8') as grade_file:
            return list(csv.reader(grade_file))

    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None

def identify_columns(headers_line:list) -> dict:
    '''Figures out what the indices of various headers are
    
    Returns a dictionary with the indices of all relevant headers.
    The intended use of this dictionary is demonstrated by the following examples:

    1. Given a line from the gradebook, for a particular student, the name of the student is found as
    name = f"{line[columns[FIRST_NAME]]} {line[columns[LAST_NAME]]}"
    
    2. Index of grade from final exam (which is unique):
    final_exam_score = line[columns[FINAL_EXAM]]

    3. Index of grades from other categories, such as projects:
    project_scores = [line[column] for column in columns[PROJECTS]]

    Does not modify the headers_line list
    '''

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
    '''Determines which category the given header belongs to

    Special care must be taken to distinguish between the normal assignments and the extra assignments.
    The header for assignment 1 begins with "Assignment 1:".
    The header for assignment 1+ begins with "Assignment 1+:"
    They share the prefix "Assignment 1"
    so checking the header for the prefix "Assignment" is not enough to distinguish between these two categories.
    '''

    for category in HEADER_PREFIXES:
        if header.startswith(HEADER_PREFIXES[category]):
            if category == ASSIGNMENTS and "+:" in header:
                return EXTRA_ASSIGNMENTS
            return category

    return "Unknown"


def display_index_dict(indices:dict, headers_line:list) -> None:
    '''Prints out the identified indices along with the corresponding headers
    
    Does not modify the indices dictionary
    Does not modify the headers_line list
    '''

    INDENT_ALIGN = 4

    print()

    for attribute in [FIRST_NAME, LAST_NAME, EMAIL, SECTION]:
        index = indices[attribute]
        print(f"{index}: {headers_line[index]}")

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
        for index in index_list:
            print(f"{index:>{INDENT_ALIGN}}: {headers_line[index]}")
    
    if FINAL_EXAM in indices:
        index = indices[FINAL_EXAM]
        print(f"{index}: {headers_line[index]}")
    else:
        print("The results from the final exam are not in yet.")


main()
