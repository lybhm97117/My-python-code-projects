"""
File: anagram.py
Name: Teresa  Tien
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    輸入word(user input的單字）,透過traversal遍歷每個user input word (EX:apple)的編碼從0-4,去找到同字母異序字
    """
    ####################
    word_list = read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break

        start = time.time()
        print('Searching...')
        found_anagrams = find_anagrams(word, word_list)
        end = time.time()
        print(f'{len(found_anagrams)} anagrams: {found_anagrams}')

    ####################

    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    word_list = []  # 建立一個空白list
    with open(FILE, 'r') as f:  # 打開一個FILE(dictionary.txt)的文件路徑，使用 r 模式（只讀模式）打開
        for line in f:  # 遊遍file中每一行
            word_list.append(line.strip())
    return word_list  # return會來的list(列表）都是字串拿掉空白＆換行字元
    #    word = line.strip() # 在每一行行尾用strip()方法切除句尾換行符號＆空白格
    #   for i in range(len(word)): # 把每一個word (EX:python都邊上編碼,從0-5號）
    #     if word[0:i+1] in vocab_dic: # 下限不包含
    #         vocab_dic[word[0:i+1]].append(word) #將這個[word 0:i+1]的字加入列表中的值
    #     else: # 如果[word 0:i+1]沒有不在voc_dic中出現過,就要創一個新的鍵值（EX: vocab_dic["ap"] = ["apple"]
    #         vocab_dic[word[0:i+1]] = [word]


def find_anagrams(s, word_list):  # s = user input的單字 EX: apple, 則len(s) =5個字
    """
    :param s:
    :return:
    """
    anagrams = []  # 創建一個空白列表 等等把找到的相似字都丟進來
    used = [False] * len(s)  # 先建立5個false的位置在list當中 因為都還沒有字母入住,等到字母入住就會從false變成True(代表有單字被使用）
    traversal(s, '', word_list, anagrams, used)
    return anagrams


def traversal(s, current, word_list, anagrams, used):  # 探索所有可能的字母組合以尋找同字母異序字, 空竹籤串起current的字,
    if len(current) != len(s):  # 長度不同要重新串單字,設定一個current空字串（竹籤）依序從s單字（EX:apple）的第一個編碼s[0]開始串,最終把apple串起來
        for i in range(len(s)):  # 遍歷s單字（EX:apple)從s[0]=a 單字開始
            if not used[i]:  # s[0]＝a is false（未被使用的狀態）
                used[i] = True  # a已經被使用,變True(讓a這個字還可以繼續被使用）
                traversal(s, current + s[i], word_list, anagrams,
                          used)  # 遞迴探索s[0]=a這個單字在word_list中, 然後用current+s[i]的竹籤串記住現在串了哪些字
                used[i] = False  # 把s[0]=a重新變成可以使用的狀態,下一個字還是可以找a
    else:  # 單字的長度相同
        if current in word_list and current not in anagrams:  # 判斷current是有效字（存在且沒出現在list中）的才把他們加進list中
            anagrams.append(current)


def has_prefix(sub_s, word_list):
    """
    :param sub_s: 以指定字串 sub_s 為開頭的單詞 EX: 'ap'
    :return:True /False, 如果都已經是False EX:'bl'但是要找‘apple'這個word,那就不必要再找下去
    """
    for word in word_list:  # 搜尋每個user輸入的word在word_list當中
        if word.startswitch(sub_s):  # 檢查當前word(EX:apple)是否是"sub_s" EX: ap開頭
            return True
    return False


if __name__ == '__main__':
    main()
