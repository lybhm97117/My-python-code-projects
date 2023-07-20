"""
File: weather_master.py
Name: Teresa Tien
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	use 'return' to decompose other variables and streamline the main function
	"""
	print('stanCode \" Weather Master 4.0 \" !')
	return sums()


def sums():
	"""
	First, separate to two cases:
	(1).input data == EXIT --> Stop the game by using 'No temperate were entered '
	(2). input number != EXIT --> continues the game

	Second, since the questions is asking 4 things by entering only one number at each time, so we should assign the
	first data into each variables to deal with each topics separately

	Highest: assign first data into "highest", then enter another "data" to compare with "highest". If wins, than the new
	data will replace to "new highest"; if not, then keep the current "highest"data without any replacement. Compares
	until enter "EXIT" number

	Lowest: methods same as "highest"

	Average temperature: comes from total temperates divide total entering days. Using "Sum = sum +data", to count each
	of the total temperates when entering each times. Using "count = count + 1, to count total amount of times entering
	data by users

	Cold days, using "cold = cold +1" when the "data" is lower than 16

	Last, print all of the data at last
	"""
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:
		print('No temperate were entered')
	else:
		highest = data
		lowest = data
		total = data
		count = 1
		avg = total / count
		cold = 0
		if data < 16:
			cold = cold + 1
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			else:
				total = total + data
				count = count + 1
				avg = total / count
				if data < 16:
					cold = cold + 1

				if data > highest:
					highest = data

				elif data < lowest:
					lowest = data
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(avg))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
