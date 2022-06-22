#This file is for unit testing purpose

"""
def get_max_test_result(): #data input and data validation

    valid_digit = False
    
    while not valid_digit:
        max_result = input("What's max test result? ")
        
        if max_result.isdigit():
            print(f"Maximum result in this test is: {max_result} p \n")
            valid_digit = True
            
        else:
            print(f"Your input is {max_result} and this is not valid number, please try again: \n")
        
    return max_result

result = get_max_test_result()
print(result)
"""

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
        result = input(f"Enter result for {name}:").split()
        name_key =  name[0]
        result_value = int(result[0])
        stud_data[name_key] = result_value
    print(stud_data)
    return stud_data

add_student_result()

print(datatype(stud_data))