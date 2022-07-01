import pandas as pd
from colorama import Fore, Back, Style


def get_test_subject():
    """
    Get the subject of the test to be used in end summary
    """
    test_subject = input("What's the subject for this test? ")
    print(f"Subject for this test is: {test_subject}\n")

    return test_subject


def get_max_test_result():
    """
    Get max test result for calculating student test performance and test stats
    Validate if input is digit. If input is not digit ask the user to enter
    valid number.
    """
    valid_digit = False

    while not valid_digit:

        max_result = input("What's max test result? ")

        if max_result.isdigit():
            print(f"Maximum result in this test is: {max_result} points \n")
            valid_digit = True

        else:
            print(
                f"Your input is {max_result} and this is not a valid number, please try again: \n")

    return int(max_result)


def add_student_result(max_result):
    """
    Add student name and result to dictionary, validate if student
    result is higher than max result.
    """
    print("Expected input for number of student is number, example 10, 24")
    records = int(input("Enter the number of students: "))

    stud_data = {}

    print("\nExpected input for name is characters, example: Eva, Dan")
    print("Expected input for result is number, example 12, 23")

    for i in range(0, records):

        name = input("\nEnter the student name :")
        result_str = input(f"\nEnter result for {name}:")
        while True:
            try:
                result = float(result_str)
                break
            except ValueError:
                print(
                    "this is not a valid number, please enter a valid number, example 10 or 9.5")
                result_str = input(f"\nEnter result for {name}:")

        while result > max_result:
            print(f"\nEntered result {result} is higher than max result")
            result_str = input(f"Enter new result for {name}:")
            result = float(result_str)

        stud_data[name] = result

    return stud_data


def calc_student_performance(data, value):
    """
    Take the input data from add student data and calculate
    the student performance based on the max_result. Use the
    performance and predefined grade levels and create a student
    test row including name, test result, performance and grade.
    Return a list of lists.
    """
    students = data
    max_result = int(value)
    stud_list_of_list = []

    for result in students.items():

        stud_perf = int((result[1] / max_result) * 100)
        student_test_perf = result + (stud_perf,)

        if stud_perf >= 90:
            student_test_row = student_test_perf + ("A",)
        elif stud_perf >= 80:
            student_test_row = student_test_perf + ("B",)
        elif stud_perf >= 70:
            student_test_row = student_test_perf + ("C",)
        elif stud_perf >= 60:
            student_test_row = student_test_perf + ("D",)
        elif stud_perf >= 50:
            student_test_row = student_test_perf + ("E",)
        else:
            student_test_row = student_test_perf + (Fore.RED + "Failed",)

        student_list = list(student_test_row)
        stud_list_of_list.append(student_list)

    return stud_list_of_list


def list_data_to_table(list_data):
    """
    converts list data to table and apply sorting on performance column
    """
    df = pd.DataFrame(
        list_data, columns=["Name", "Test Result", "Performance", "Grade"])
    perfor_sort = df.sort_values(by="Performance", ascending=False)

    return perfor_sort


def main():
    """
    Run all program functions
    """

    get_test_subject()
    max_result = get_max_test_result()
    stud_data = add_student_result(max_result)
    print(stud_data)
    stud_list_of_list = calc_student_performance(stud_data, max_result)
    student_perfor_table = list_data_to_table(stud_list_of_list)
    print(student_perfor_table)
    return student_perfor_table


main()
