"""
File: boggle.py
Name: Teresa Tien
----------------------------------------
This program simulates a classic game, boggle.
In the beginning, we allow users to input the
combination of sixteen letters (4x4). Then,
we will find out all the answers recursively.
During the process of searching, as soon as a
word is found, it will print "Found: 'word'"
in the Python console. After finding out all
the possible answers, this program will show
how long the searching process is and terminate
the program.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	1. Create a 4*4 board and user needs to fill in the alphabet
	2. find words that matches the word in the dictionary
	3. Print out the founded words
	"""
	start = time.time()
	####################
	board = get_board() 	# user需要填入符合規定的16個數字才可以啟動遊戲
	word_list = read_dictionary()
	words = find_word(board, word_list)
	print_found_words(words)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_board():
	"""
	:return: 4*4 字母盤
	"""
	board = [] 	# 把4*4字母盤儲存在這個list當中
	for i in range(1, 5):
		row = input(f'{i} row of letters: ')
		if len(row) == 7 and len(row.split()) == 4:
			row = row.lower().split() 	# 需要將字串處理後的結果用一個新的符號row來表示,不然處理後的字串無法被保存
		else:
			print('Illegal input')
			break
		board.append(row)
	return board


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_list = []  # 建立一個空白list 把dictionary中的字都掉空白＆換行字元 存在這個列表中
	with open(FILE, 'r') as f:
		for line in f:
			word_list.append(line.lower().strip())
	return word_list


def has_prefix(sub_s, word_list): 	# sub_s是前綴單字 EX: Apple中的‘ap'
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_list:
		if word.startswith(sub_s):
			return True
	return False


def find_word(board, word_list):
	"""
	在 4x4 字母盤上搜尋所有可以被串連起來的英文單字
	"""
	words = [] 	# 把找到的单词儲存在這個list(列表）中
	visited = [[False] * 4 for _ in range(4)] 	# 創建一個4*4的矩陣 沒訪問過就是False,有尋訪過就是True
	for i in range(4):
		for j in range(4):
			helper(board, word_list, i, j, '', visited, words) 	# 用helper function來尋訪每一個經過(i&j)的單字,用空字串來串初始單字,並把每一個經過的
			# 的單字visited都從false變true,最後把找到的這些字都存在words的列表中
	words = [word for word in words if word in word_list] 	# 只抓取words列表和word_list列表中重複的單字,儲存在新的words 列表中
	return words


def helper(board, word_list, row, col, word, visited, words): 	# 做traversal 追蹤遍歷其他格字的字 找尋word_list中存在的單字
	if row < 0 or row > 3 or col < 0 or col > 3: 	# 每一行列編碼都是0-3,超出4*4範圍就直接不看了 return
		return
	if visited[row][col]: 	# 已經訪問過的就不再做traversal
		return
	word += board[row][col]  	# 把board[row][col]現在這個位置的單字加入word當中 ,EX: 'ap' 多串一個變成‘app'
	if not has_prefix(word, word_list): 	# 前綴字EX: 'ap'沒有的就不用繼續做traversal
		return
	if len(word) >= 4 and word not in words:
		words.append(word) 	# 超過四個字以上且沒在words 列表中出現過的word, 就要加進words list當中(EX: roomy)
	visited[row][col] = True 	# 已經訪問過的位置就不能再經過
	for i in range(-1, 2): 	# 該[row][col]這個位置是(0,0)的話,他的相鄰8個位置的編碼分別是(-1,-1), (-1,0), (-1, 1)..一路到(1,1).而上限2不包含
		for j in range(-1, 2):
			helper(board, word_list, row+i, col+j, word, visited, words) 	# 相鄰字在做traversal把word_list中有的字母串起來
	visited[row][col] = False 	# 這一次traversal做完,訪問過的字都要再回覆到False(未被訪問的狀態）讓下一個循環可以重新被放問


def print_found_words(words):
	"""
	:param words:
	:return: 輸出最後找到的單字
	"""
	for word in words:
		print(f'Found "{word}"')
	print(f'There are {len(words)} words in total.')

if __name__ == '__main__':
	main()
