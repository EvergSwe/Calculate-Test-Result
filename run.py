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
    """
    max_result = input("What's max test result? ")
    print(f"Maximum result in this test is: {max_result} p\n")

    return max_result

def main():
    """
    Run all program functins
    """
    get_test_subject()
    get_max_test_result()

main()
