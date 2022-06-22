#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#itertools combinations module can be used to produce combination tuples in sorted order.
#combinations(iterable, r) - it will return r length tuples with no repeated outcomes for each combination, if each element is unique.
import itertools
from itertools import combinations

#Input
number_of_people = int(input("How many people are there? "))

if number_of_people <= 1:
    print("That number cannot be used for a pair.")

else:
    #Create list to add range of numbers to the list
    number_list = []
    #There is +1 for the variable number_of_people to numbers from 1 to the input for the number_of_people.
    number_list.extend(range(1, number_of_people + 1))

    #Used to produce 2 length tuples with no repeated outcomes
    comb = combinations(number_list, 2)

    #* asterisk operator can be used to unpack objects which removes the brackets when printing
    #For loop is used to print all the possible combinations
    for i in comb:
        #Output
        print(*i)
