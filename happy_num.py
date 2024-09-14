
# Check if a number is a happy number.

# Args:
#     num (int): The number to be checked.

# Returns:
#     bool: True if is a happy number, False otherwise.
def happy_num(num_to_check):
    # as receives a number, it's necesary convert to string to be split
    num_to_check = str(num_to_check)
    numbers_evaluated = [] 
    is_happy = False
    while(num_to_check not in numbers_evaluated):
        numbers_evaluated.append(num_to_check)
        # divides the number into individual digits
        list_to_check = list(num_to_check)
        sum = 0
        for i in list_to_check:
            sum = sum + int(i) ** 2
        if(sum == 1):
            is_happy = True
            return is_happy
        else:
            num_to_check = str(sum)
    return is_happy

# Main function asks for a number to be checked and indicates if is or not a happy number.
# Raises:
#         Print a warning if the value to be checked is not numeric
def main():
    try_again = True
    while(try_again):
        user_input = input("Enter a number: ")
        try:
            if happy_num(int(user_input)):
                print(user_input, "IS A HAPPY NUMBER")
            else: 
                print(user_input, "IS NOT HAPPY NUMBER")
        except ValueError:
            print("Invalid input. Please enter a valid number.")  

        question = input("Do you want to try again? Enter 'y' or 'n': ")
        if question == "y": 
            try_again = True
        else:
            try_again = False   


# call to main function
main()
