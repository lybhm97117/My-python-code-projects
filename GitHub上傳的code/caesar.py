"""
File: caesar.py
Name: Teresa Tien
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    1. 題目給的alphabet是原先的字串,須重新定義一個old_alphabet(依據secret number數字的不同，分成前半段＆後半段）
    2. 加密的數字一個一個去跑for j in range (0, len(old_alphabet)),當字母吻合的時候把這個英文字的[i]序號串到空字串的牙籤上alphabet的字串裡
    """
    move = int(input('Secret Number: '))
    cip = input("What's the ciphered string?").upper()
    front = ALPHABET[len(ALPHABET)-move:]
    back = ALPHABET[0: len(ALPHABET)-move]
    old_alphabet = front + back

    string = ''
    for i in range(0, len(cip)):
        if cip[i].isalpha():
            string += ALPHABET[old_alphabet.find(cip[i])]
        else:
            string += cip[i]
    print('The ciphered string is: ' + str(string))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
