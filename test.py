def get_max_test_result():
    """
    Get max test result for calculating student test performance and test stats
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
    
result = get_max_test_result()
print(result)