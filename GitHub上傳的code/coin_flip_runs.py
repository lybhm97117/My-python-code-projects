"""
File: coin_flip_runs.py
Name: Teresa Tien
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	1.設一個開關 預設是0=關著,如果前字跟後字ㄧ樣就會打開開關變1, 繼續下一個字,如果下一個字又跟前者一樣,開關仍然打該不會關起來,要等下一個字跟
	前一個不一樣了開關才要關起來變成0.
	2.	同時計算開關開啟和關閉的次數。從關-->開-->關 算一次 總共會跑"Number of runs"的次數
	"""
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	same = 0
	string = ''  # 不要用'str'因為是已經內建的variables, 所以用其他字代替
	old_str = ''
	switch = 0  #
	while same < num_run:
		random = r.choice(['H', 'T'])  # random.choice(seq) = 在序列seq中随机抽取一个值
		if random == old_str:
			if switch == 0:
				same += 1
			switch = 1  # open

		else:
			switch = 0  # close
		string += random
		old_str = random
	print(string)







# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
