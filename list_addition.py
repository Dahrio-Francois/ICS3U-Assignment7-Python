#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# This program will calculate the sum of integers
#   in a list


def calculation(group):
    # this function does the final calculations

    total = 0

    length = len(group)

    while length > 0:

        length = length - 1
        total = total + group[length]

    return total


def main():
    # this calculates the sum of the list

    group = []

    loop_counter = 0

    number_amount = int(input("How many numbers would you like to add: "))

    try:
        while loop_counter < number_amount:
            integer_from_user = int(input("Enter in an integer to join the list: "))
            print("")
            loop_counter = loop_counter + 1
            group.append(integer_from_user)

        print("")
        print(group)
    except Exception:
        print("\nThat was not a valid integer, please try again.")

    print("\nThe sum of the numbers in that list is {}".format(calculation(group)))


if __name__ == "__main__":
    main()
