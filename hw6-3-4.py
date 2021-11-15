# Author: ATN 11/15/21

sequence_in = input("Please enter a list of numbers or letters: ")

sequence = list(sequence_in)
sequence_in.split()

choice = input("Would you like the 'middle' or 'ends' or this list? ")

if(choice == "ends"):
    ends = str(sequence_in[0:1]) + str(sequence_in[-1])
    print("Your text is: {0}".format(ends))
elif(choice == "middle"):
    middle = str(sequence_in[1:-1])
    print("Your text is: {0}".format(middle))
else:
    print("Incorrect command.")
