
def is_div_by(num, div):
    """
    Check if a number is divisible by another number.

    Args:
        num (int): The number to be checked.
        div (int): The number divisor.

    Returns:
        bool: True if a number is divisible by a divisor, False otherwise.
    """
    if num % div == 0 : 
        return True
    return False

def foo_bar():
    """
    Print "FooBar" is a number is divisible by 3 and 5, print "Foo" if is only divisible by 3, 
    print "Bar" if is only divisible by 5 or print the number if it is not divisible by 3 either by 5.

    Raises:
        Print a warning if the value to be checked is not numeric
    """
    try_again = True

    while(try_again):
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            response = number
            if is_div_by(number, 3) and is_div_by(number, 5):
                response = "FooBar"
            elif is_div_by(number, 3):
                response = "Foo"
            elif is_div_by(number, 5):
                response = "Bar"
            print(response)
        except  ValueError:
            print("Invalid input. Please enter a valid number.")    

        question = input("Do you want to try again? Enter 'y' or 'n': ")
        if question == "y": 
            try_again = True
        else:
            try_again = False


# call to main function
foo_bar()
