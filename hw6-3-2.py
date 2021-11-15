# Author: ATN 11/15/21

num_input = input("Please type a sequence of numbers: ")

num_sorted = list(num_input)
num_sorted.sort()

if(num_sorted == list(num_input)):
    print("The numbers {0} are sorted numerically.".format(num_input))
else:
    print("The numbers {0} are not sorted numerically".format(num_input))
