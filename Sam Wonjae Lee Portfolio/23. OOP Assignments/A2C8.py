#Sam Wonjae Lee

import random

class Die():
    def __init__(self, sides = 6):   
        """Attributes for owner and sides"""

        self.owner = "Sam Lee"
        self.sides = sides

    def greet_owner(self):
        """Prints a message for owner"""
        
        print(f"Hello {self.owner}!")

    def roll_die(self):    
        """ Prints a random from 1 to the number of sides"""
        
        print(random.randint(1, self.sides))

dieOne = Die()
dieOne.greet_owner() #Greets owner

#Prints 6-sided die
print("Rolling six sided die 10 times:")
for i in range(10):
    dieOne.roll_die()

#Prints 10-sided die
print("Rolling ten sided die 10 times:")
dieTwo = Die(sides = 10)
for j in range(10):
    dieTwo.roll_die()

#Prints 20-sided die
print("Rolling twenty sided die 10 times:")
dieThree = Die(sides = 20)
for k in range(10):
    dieThree.roll_die()

    
