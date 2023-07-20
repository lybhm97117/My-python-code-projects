"""
File: largest_digit.py
Name: Teresa Tien
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number entered by the user.
	:return: recursion, compare the largest number in the number position.
	--------------------------------
	Thinking:
		1. Two numeric variables are needed to compare the size of the two.
		2. The last position of the number is given priority,
			so the concept of "remainder" is used to take out the last position.

	Step:
		1.  If the value of n passed in is negative, first convert it to a positive value.
	"""

	# if n < 0:
	# 	n = -n  # 將負數轉換為正數進行處理
	# if n < 10:
	# 	return n  # 如果只有一位數，該位數就是最大數
	# last_digit = n % 10  # 取得最後一位數字
	# remaining_digits = n // 10  # 剩下的前面幾個數
	# max_digit = find_largest_digit(remaining_digits)  # 遞迴找出剩餘數字中的最大數字
	# if last_digit > max_digit:
	# 	return last_digit  # 如果最後一位數字比剩餘數字中的最大數字大，則回傳最後一位數字
	# else:
	# 	return max_digit  # 否則回傳剩餘數字中的最大數字
	# 以下有更好的寫法
	if n < 0:
		n = -n 	# 將負數轉換為正數進行處理
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, num):
	"""
		:param n: int, the number entered by the user.
		:param find_  largest_ digit_ helper: int, compare the largest number in the number position.
		:return largest_digit: int, compare the largest number in the number position.
		------------------------------------------------
	"""
	last_digit = n % 10 	# 取得最後一位數字
	if n < 10:
		if num > n:
			return num  # 如果只有一位數，該位數就是最大數
		else:
			return n
	else:
		if last_digit > num:
			num = last_digit
		remaining_digits = n // 10  # 剩下的前面幾個數
		return find_largest_digit_helper(remaining_digits, num)


if __name__ == '__main__':
	main()
