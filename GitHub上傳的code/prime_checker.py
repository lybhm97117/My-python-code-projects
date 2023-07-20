"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100
def main():
	"""
	First, separate to two cases:
	(1).input number == EXIT --> Stop the game by using 'Have a good one! '
	and input number != EXIT --> continues the game
	Second,
	(1).prime number means : number "n" cannot well divide all its smaller numbers, use "for i in range" to count i from
	2 to n-1
	(2). non-prime number means: number "n" can divide at least one number that is smaller than itself

	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))

	while True:
		if n == EXIT:
			print('Have a good one! ')
			break
		else:
			for i in range(2, n):
				if (n % i) == 0:
					print(str(n) + ' is not a prime number')
					n = int(input('n: '))
					break  # need to jump out of this loop; otherwise, the next n will still in "the for i in range loop"
					# and count from i=3
			else:  # if all the "for i in range" doesn't work, then will go into this "else" block
				print(str(n) + ' is a prime number')
				n = int(input('n: '))





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
