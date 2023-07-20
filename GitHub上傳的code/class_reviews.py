"""
File: class_reviews.py
Name: Teresa Tien
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    There are 3 conditions that need to be considered.
    1. if there are sc001/sc101 scores, and then user press '-1', then the jump out of the calculation and press related results
    2. if there's isn't any sc001 & sc101 scores, but the user press '-1' at first, then shows:'No class scores were entered'
    3. if user fill in  sc001/sc101 scores and do not press '-1', then calculate max, min, and average scores
    """
    max_sc001 = float('-inf')  # 初始值設成負無限大,所以任意輸入數字都會大於這個值
    min_sc001 = float('inf')  # 初始值設成無限大,所以任意輸入數字都會小於這個值
    sum_sc001 = 0
    count_sc001 = 0
    max_sc101 = float('-inf')
    min_sc101 = float('inf')
    sum_sc101 = 0
    count_sc101 = 0

    while True:
        class_name = str(input('Which class?')).upper()
        if count_sc001 == 0 and count_sc101 == 0 and class_name == '-1':
            break
        else:
            score = int(input('Score: '))
            if class_name == 'SC001':
                max_sc001 = max(max_sc001, score)
                min_sc001 = min(min_sc001, score)
                sum_sc001 += score
                count_sc001 += 1
            elif class_name == 'SC101':
                max_sc101 = max(max_sc101, score)
                min_sc101 = min(min_sc101, score)
                sum_sc101 += score
                count_sc101 += 1

    if count_sc001 == 0 and count_sc101 == 0 and class_name == '-1':
        print('No class scores were entered')
    else:
        print('=============SC001=============')
        if count_sc001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_sc001))
            print('Min (001): ' + str(min_sc001))
            print('Avg (001): ' + str(sum_sc001 / count_sc001))

        print('=============SC101=============')
        if count_sc101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_sc101))
            print('Min (101): ' + str(min_sc101))
            print('Avg (101): ' + str(sum_sc101 / count_sc101))


















# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
