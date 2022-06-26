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

"""
def add_student_result():

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
"""

"""
def calc_student_performance():
    
    max_result = 98
    students = {"eva":90, "bob":85, "maria":72, "grace":63, "dan":51, "eric":43}
    students_list = []
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
            student_test_row = student_test_perf + ("Failed",)
        
        student_list = list(student_test_row)
        stud_list_of_list.append(student_list)
    print(stud_list_of_list)


calc_student_performance()
"""

def list_data_to_table():

    import pandas as pd

    list_data = [['eva', 90, 91, 'A'], ['bob', 85, 86, 'B'], ['maria', 72, 73, 'C']
    , ['grace', 63, 64, 'D'], ['dan', 51, 52, 'E'], ['eric', 43, 43, 'Failed']]
    
    df = pd.DataFrame(list_data, columns = ["Name", "Test Result", "Performance", "Grade"])
    perfor_sort = df.sort_values(by="Performance", ascending=False)
    print(perfor_sort)

list_data_to_table()
