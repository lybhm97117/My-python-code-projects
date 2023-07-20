"""
File: hailstone.py
Name: Teresa Tien
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    First, separate the question to 2 parts.
    (1). enter number 1 to stop the game
    (2). enter numbers w/o 1 to continue other calculation

    Second, determine the number is even or odd. Then follow the rule of cutting half or 3n+1

    Last, counts how many times that this number's calculation needs. Every time when the number
    go through the while loop, the calculation will +1, regardless of going through odd-path or
    even-path.
    """
    print('This program computes Hailstone sequences.')  # Welcome banner
    num = int(input('Please enter a number: '))  # Get the number to be calculated

    steps = 0  # Counter for how many steps it takes to make the number become 1

    while True:
        if num == 1:  # Check if to finish processing
            break

        if num % 2 == 1:  # Odd
            print(str(num) + ' is odd, so I make 3n+1: ' + str(3 * num + 1))
            num = 3 * num + 1
        else:  # Even
            print(str(num) + ' is even, so I take half: ' + str(num // 2))
            num = num // 2

        steps += 1

    print('It took ' + str(steps) + ' steps to reach 1.')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
