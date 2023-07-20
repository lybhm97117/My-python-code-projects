"""
File: quadratic_solver.py
Name: Teresa Tien
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	First input integer a,b and c. Then determine whether  y (=b * b - 4 * a * c) is positive, zero, or negative.
	Ｗe cannot first square root the number because if the number is negative, then the number violates the basic math
	rules: numbers inside the square root cannot be negative.

	Secondly, separate to 3 conditions: y>0, y ==o, and y <0
	if y <0, we don't need to do the square root but instead print "No real roots"
	"""
	print('stanCode Quadratic Solver !')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	y = b * b - 4 * a * c
	# 不能先開根號 因為如果先開發現是負值 還不用跑下面程式 在這一行直接當掉了＃所以先決定y的正負值再決定要不要開根號

	if y > 0:
		z = math.sqrt(y)
		x1 = (-b + z) / (2 * a)
		x2 = (-b - z) / (2 * a)
		print('Two roots: ' + str(x1) + " , " + str(x2))

	elif y == 0:
		z = math.sqrt(y)
		x1 = (-b - z) / (2 * a)
		print('One roots: ' + str(x1))

	else:
		print('No real roots ')











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
