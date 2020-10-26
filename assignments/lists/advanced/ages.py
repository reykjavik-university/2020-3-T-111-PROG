from operator import itemgetter


def gather_all_inputs() -> list:
    number_of_people = ask_for_number_of_people()
    names_and_ages = gather_names_and_ages(number_of_people)
    return names_and_ages


def ask_for_number_of_people() -> int:
    return ask_for_integer("Number of people: ")


def ask_for_integer(text: str) -> int:
    while True:
        value_str = input(text)
        try:
            return int(value_str)
        except ValueError:
            print(f"{value_str} is not an integer. Please try again.")


def gather_names_and_ages(how_many: int) -> list:
    names_and_ages = []
    for i in range(1, how_many + 1):
        name = input(f"Name of person {i}: ")
        age = ask_for_integer(f"Age of person {i}: ")
        names_and_ages.append([name, age])
    return names_and_ages


def show_oldest_and_youngest_persons(names_and_ages: list):
    oldest_person, max_age = find_oldest_person(names_and_ages)
    print(f"The oldest person is {oldest_person} who is {max_age} years old")
    youngest_person, min_age = find_youngest_person(names_and_ages)
    print(f"The youngest person is {youngest_person} who is {min_age} years old")


def find_oldest_person(names_and_ages: list):
    name, age = max(names_and_ages, key=itemgetter(1))
    return name, age


def find_youngest_person(names_and_ages: list):
    name, age = min(names_and_ages, key=itemgetter(1))
    return name, age


def show_central_tendency_measures(names_and_ages: list):
    PRECISION = 2
    median_age = determine_median_age(names_and_ages)
    print(f"The median age is {round(median_age, PRECISION)}")
    average_age = determine_average_age(names_and_ages)
    print(f"The average age is {round(average_age, PRECISION)}")


def determine_median_age(names_and_ages: list) -> float:
    mid_start_index = (len(names_and_ages) - 1) // 2
    mid_stop_index = (len(names_and_ages) // 2) + 1
    sorted_by_age = sorted(names_and_ages, key=itemgetter(1))
    middle_elements = sorted_by_age[mid_start_index:mid_stop_index]
    return determine_average_age(middle_elements)


def determine_average_age(names_and_ages: list) -> float:
    # The following line uses list comprehension. See chapter 7.11
    just_ages = [row[1] for row in names_and_ages]
    average_age = sum(just_ages) / len(just_ages)
    return average_age


def main():
    names_and_ages = gather_all_inputs()
    show_oldest_and_youngest_persons(names_and_ages)
    show_central_tendency_measures(names_and_ages)


main()
