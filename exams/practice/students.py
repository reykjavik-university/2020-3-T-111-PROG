NUMBER_OF_STUDENTS = 4
NUMBER_OF_GRADES = 3

def create_student_dict():
    ''' Creates a dictionary with students names as keys and a list of grades as values'''
    student_dict = {}
    for _ in range(NUMBER_OF_STUDENTS):
        name = input("Student name: ")
        grades = []
        for j in range(NUMBER_OF_GRADES):
            grade = input("Input grade number {}: ".format(j+1))
            grades.append(float(grade))
        student_dict[name] = grades
    return student_dict


def print_students(students_dict):
    ''' Prints the grades of each student '''
    print("Student list:")
    for student in sorted(students_dict.keys()):
        print("{}: {}".format(student, students_dict[student]))


def get_student_with_highest_average_grade(students_dict):
    ''' Finds the student with the highest average.
        Returns both the student name and the corresponding average grade '''
    highest_average_grade = 0.0
    name = ""
    for student, grades in sorted(students_dict.items()):
        average_grade = sum(grades) / len(grades)
        if average_grade > highest_average_grade:
            highest_average_grade = average_grade
            name = student
    return (name, highest_average_grade)

def main():
    students_dict = create_student_dict()
    print_students(students_dict)
    name, average_grade = get_student_with_highest_average_grade(students_dict)
    print("Student with highest average grade:")
    print("{} has an average grade of {:.2f}".format(name,average_grade))

main()