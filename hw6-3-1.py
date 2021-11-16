# Author: ATN 11/16/21

ana_input = input("Please write any word/phrase: ")
ana_input_2nd = input("Please write another word/phrase: ")

ana_sorted = list(ana_input)
ana_sorted.sort()
ana_sorted_2nd = list(ana_input_2nd)
ana_sorted_2nd.sort()

if(ana_sorted == ana_sorted_2nd):
    print(
        "The word {0} is an anagram of {1}."
        .format(ana_input, ana_input_2nd)
        )
else:
    print(
        "The word {0} is not an anagram of {1}."
        .format(ana_input, ana_input_2nd)
        )
