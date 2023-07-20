"""
File: complement.py
Name: Teresa Tien
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    分兩種狀況：
    （1).輸入的是英文字
    依照原先輸入的英文字重新串成對應的英文字（ＥＸ：Ａ變Ｔ）

    (2).空字串, print 'DNA strand is missing.'
    """

    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna.isalpha():
        string = ''  # 安排空牙籤
        for letter in dna:
            if letter == 'A':
                string += 'T'
            elif letter == 'T':
                string += 'A'
            elif letter == 'C':
                string += 'G'
            elif letter == 'G':
                string += 'C'
        return string
    else:
        print('DNA strand is missing.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
