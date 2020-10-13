FILE_NOT_FOUND_MESSAGE = "File {} not found"

def open_file(filename):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None

def get_file_object(prompt):
    '''Prompts the user for a file name and return the associated file object'''
    file_name = input(prompt)
    file_object = open_file(file_name)
    return file_object, file_name

def convert_to_floats(str_list):
    '''Convert the given list of strings to a list of floats'''
    float_list = [ float(a_str) for a_str in str_list]
    return float_list    

def get_parts(file_object):
    '''Reads a file consisting of course assessment info in two lines:
        part_1 part_2 ... part_n
        weight_1, weight_2, ... weight_n
        and returns the data as a list of lists:
        [ (part_1, weight_1), (part_2, weight_2), ..., (part_n, weight_n)]'''
    
    parts = file_object.readline().split()
    weights = convert_to_floats(file_object.readline().split())

    tuples_list = []
    for idx, part in enumerate(parts):
        tuples_list.append((part, weights[idx]))

    return tuples_list

def get_grades(file_object):
    '''Reads the grades from a file.  Each line contains:
    student_id grade_part_1 grade_part_2, ..., grade_part_n
    Returns the data in list of tuples:
    [   (student_1, [grade_part_1 grade_part_2, ..., grade_part_n]),
        (student_2, [grade_part_1 grade_part_2, ..., grade_part_n]), 
        ...
        (student_n, [grade_part_1 grade_part_2, ..., grade_part_n])
    ]'''
    all_students_grades_list = [] 
    for line in file_object:
        data_list = line.split()
        student_id = data_list[0]
        grades_list = convert_to_floats(data_list[1:])
        all_students_grades_list.append((student_id, grades_list))
    
    return all_students_grades_list

def compute_final_grade(parts_list, grade_list_for_student):
    '''Computes the weighted final based on the given student grades and the
        weights given in the parts_list'''

    final_grade = 0
    for idx, grade in enumerate(grade_list_for_student):
        # The weight is in the second part of the tuple
        final_grade += grade * parts_list[idx][1]  
    
    return final_grade

def add_final_grades(parts_list, grades_list):
    '''Adds the final grade for each studenet to grades_list'''
    # Each grade_info is a tuple:
    # (student_i, [grade_part_1 grade_part_2, ..., grade_part_n])
    for idx, grade_info in enumerate(grades_list):
        student_id, student_grades = grade_info
        final_grade = compute_final_grade(parts_list, student_grades)
        # Add the final grade to the current grade info
        grades_list[idx] = (student_id, student_grades, final_grade)

def print_all_results(parts_list, grades_list):
    WIDTH_ID = 16
    WIDTH_GRADE = 14
    DIGITS = 2

    print()
    print(f'{"Student ID":>{WIDTH_ID}}', end=")
    for part in parts_list:
        print(f'{part[0]:>{WIDTH_GRADE}}', end=")
    print(f'{"Course grade":>{WIDTH_GRADE}}')

    for grades_info in grades_list:
        print(f'{grades_info[0]:>{WIDTH_ID}}', end=") # Student name
        grades_for_parts = grades_info[1]
        for part_grade in grades_for_parts:
            print(f'{part_grade:>{WIDTH_GRADE}}', end=")
        print(f'{round(grades_info[2],DIGITS):>{WIDTH_GRADE}}') # Course grade
        

def process_student_grades(parts_list):
    '''Processes student grades and prints out the result '''
    grade_file_object, file_name = get_file_object("Enter filename for grades: ")
    if grade_file_object != None:
        grades_list = get_grades(grade_file_object)
        grade_file_object.close()
        print(grades_list)
        
        add_final_grades(parts_list, grades_list)
        print(grades_list)
        print_all_results(parts_list, grades_list)
    else:
        print(FILE_NOT_FOUND_MESSAGE.format(file_name))

# Main program starts here
parts_file_object, file_name = get_file_object("Enter filename for parts: ")
if parts_file_object != None:
    parts_list = get_parts(parts_file_object)
    parts_file_object.close()
    print(parts_list)   
    process_student_grades(parts_list) 
else:
    print(FILE_NOT_FOUND_MESSAGE.format(file_name))
