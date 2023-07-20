"""
File: hangman.py
Name: Teresa Tien
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    分成四個part:
    Part 1: print 出 introduction(題目固定開頭問句）
    Part 2: 猜對字的情況．會再分成已全部猜完＆還有數字沒有猜完
    Part 3: 猜錯字的情況 分成猜錯但還可以在猜 ＆已經沒有命可以猜了
    p.s.目前hangman跑出來會有bug>< 解不掉ＱＱ

    """
    string = ''     # 建立空牙籤
    word = random_word()
    life = N_TURNS
    for i in range(len(word)):  # 先串出題目指示的“------“樣式
        string += '-'
    print('The word looks like: ' + str(string))
    print('You have ' + str(life) + ' guesses left.')  # 以上是part one
    while True:
        guess = input('Your guess: ').upper()
        if not guess.isalpha() or len(guess) > 1:
            print('illegal format.')    # 處理illegal情況,並且不減少壽命
        elif guess in word:   # 猜對英文字,但會有幾種情框：猜對/重複猜
            new_string = ''
            for i in range(len(string)):
                if guess == word[i]:
                    new_string += guess   # 猜對的單字就在空牙籤上串上該猜對的字
                elif string[i].isalpha():   # 前幾輪猜對的字需要保留
                    new_string += string[i]
                else:                          # concatenating unknown word with -
                    new_string += '-'
            string = new_string
            print('You are correct!')
            if '-' not in string:  # 前面英文字都猜對,且已經猜完數字
                print('You win!!')
                print('The word was: ' + str(string))
                break
            else:
                print('The word looks like: ' + str(string))  # 前面英文字都猜對,但還沒猜完要繼續猜
                print('You have ' + str(life) + ' guesses left. ')  # Part 2（猜對）情況結束
        else:   # 以下是猜錯情況
            life -= 1
            print('There is no ' + str(guess) + "'s in the word")
            if life != 0:   # 分成雖然猜錯 但是還有命可以猜
                print('The word looks like: ' + str(string))
                print('You have ' + str(life) + ' guesses left.')

            else:    # 猜錯 而且已經完全沒有命可以猜了
                print('You are completely hung : (')
                print('The word was: ' + str(word))
                break























def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
