# Author: ATN 11/15/21

numbers_in = input("Please enter five numbers: ")

numbers = list(numbers_in)
numbers.sort()
numbers[0:4] = []

total = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3]) + int(numbers[4])
print("The sum of these numbers is {0}.".format(total))
