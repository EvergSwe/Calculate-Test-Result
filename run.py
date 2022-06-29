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
                f"Your input is {max_result} and this is not valid number, please try again: \n")

    return int(max_result)


def add_student_result(max_result):
    """
    Add student name and result to dictionary
    """
    print("Expected input for number of student is number, example 10, 24")
    record = int(input("Enter the number of students: "))

    stud_data = {}

    print("\nExpected input for name is characters, example: Eva, Dan")
    print("Expected input for result is number, example 12, 23")

    for i in range(0, record):

        name = input("Enter the student name :")
        result_str = input(f"Enter result for {name}:")
        result = int(result_str)

        while result > max_result:
            print(f"Entered result {result} is higher than max result")
            result_str = input(f"Enter new result for {name}:")
            result = int(result_str)

        stud_data[name] = result
        print(stud_data)

    return stud_data

def calc_student_performance(data, value):
    """
    Take the input data from add student data and calculate the student performance based
    on the max_resultuse. Use the performance and predefined grade levels and create a student
    test row including name, test result, performance and grade. Return a list of lists.
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
        print(student_list)
        stud_list_of_list.append(student_list)

    return stud_list_of_list


def list_data_to_table(data):
    """
    converts list data to table and apply sorting on performance column
    """

    df = pd.DataFrame(
        data, columns=["Name", "Test Result", "Performance", "Grade"])
    perfor_sort = df.sort_values(by="Performance", ascending=False)

    return perfor_sort


def main():
    """
    Run all program functions
    """
    get_test_subject()
    max_result = get_max_test_result()
    stud_data = add_student_result(max_result)
    stud_list_of_list = calc_student_performance(stud_data, max_result)
    student_perfor_table = list_data_to_table(stud_list_of_list)
    print(student_perfor_table)
    return student_perfor_table


main()
