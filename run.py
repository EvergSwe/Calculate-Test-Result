# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_test_subject():
    """
    Get the subject of the test to be used in end summary 
    """
    test_subject = input("What's the subject for this test? ")
    print(f"Subejct for this test is: {test_subject}\n")

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
            print(f"Maximum result in this test is: {max_result} p \n")
            valid_digit = True
            
        else:
            print(f"Your input is {max_result} and this is not valid number, please try again: \n")
        
    return max_result

def add_student_result():
    """
    Add student name and result to dictunary 
    """
    
    record = int(input("Enter the number of students: "))

    stud_data={}

    for i in range(0,record):
        name = input("Enter the student name :").split()
        result = input(f"Enter result for {name}:").split()
        name_key =  name[0]
        result_value = int(result[0])
        stud_data[name_key] = result_value
    print(stud_data)
    return stud_data


def main():
    """
    Run all program functions
    """
    get_test_subject()
    get_max_test_result()
    #add_student_result()

main()

