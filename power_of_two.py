#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 3, 2022
# This program asks the user for a positive number and squares
# all of the integers from 0 to the user number using a for-loop
# It will then display the squared numbers to the user


def main():
    # Initialize Variable
    squared_number = 0

    # Asks for a number
    user_number_string = input("Enter a whole number: ")

    # Displays empty line
    print("")

    # Checks for exceptions
    try:
        # Converts user number to integer
        user_number = int(user_number_string)

    # In the event of an Exception
    except Exception:
        print(f"{user_number_string} is not a whole number!")

    # If there are no exceptions
    else:

        # If the user enters a negative number
        if user_number < 0:
            print(f"{user_number} is not a whole number.")

        # If the user entered a valid number
        else:

            # Squares every number up to the user number
            for counter in range(0, user_number + 1):
                # Squares the user number
                squared_number = counter**2
                # Displays the squared number to user
                print(f"{counter}^2 = {squared_number}")

    # Message displayed to user regardless of input
    finally:
        print("\nThank you for using the program!")


if __name__ == "__main__":
    main()
