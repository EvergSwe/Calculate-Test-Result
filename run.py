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
        global max_result
        max_result = input("What's max test result? ")
        
        if max_result.isdigit():
            print(f"Maximum result in this test is: {max_result} p \n")
            valid_digit = True
            
        else:
            print(f"Your input is {max_result} and this is not valid number, please try again: \n")
        
    return max_result


def add_student_result():
    """
    Add student name and result to dictionary
    """
    print("Expected input for number of student is number, example 10, 24")
    record = int(input("Enter the number of students: "))

    stud_data={}

    print("\nExpected input for name is characters, example: Eva, Dan")
    print("Expected input for result is number, example 12, 23")

    for i in range(0,record):
        name = input("Enter the student name :").split()
        result = input(f"Enter result for {name}:").split() #add input check result is not > max result
        name_key =  name[0]
        result_value = int(result[0])
        stud_data[name_key] = result_value

    return stud_data

def calc_student_performance(data, value):
    """
    Take the input data from add student data and max_result value and calculate the student performance and
    grade according to predefined levels.
    """
    students = data
    max_result = int(value)
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
                student_test_row = student_test_perf + ("Failed",)
            
            print(student_test_row)

def main():
    """
    Run all program functions
    """
    get_test_subject()
    max_result = get_max_test_result()
    stud_data = add_student_result()
    students_performance = calc_student_performance(stud_data, max_result)
    
main()