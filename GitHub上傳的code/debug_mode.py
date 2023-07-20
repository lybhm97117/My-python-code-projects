"""
File: debug_mode.py
Name: Teresa Tien
-----------------------------
This file demonstrates PyCharm Debug Mode.
Students will set several breakpoints and
press 'Resume Program' to debug
"""


def main():
    counter = 3
    for i in range(1000):
        for j in range(100):
            for k in range(10):
                counter += 0.01
    counter /= 2                      # Answer1: 10003.000000171922
    do_not_step_into(counter)
    counter /= 2
    print(counter)                    # Answer2: 2500.7500000429804


def do_not_step_into(counter):
    for i in range(10):
        for j in range(100):
            for k in range(1000):
                counter += 1


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
