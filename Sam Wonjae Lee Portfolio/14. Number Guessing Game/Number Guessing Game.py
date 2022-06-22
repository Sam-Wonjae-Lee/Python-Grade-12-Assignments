#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#random module is used to return a random number from a range of numbers.
import random

#attempt counter
attempts = 1
#Computer will choose a random number between 1 to 100
computer_choice = random.randint(1,100)
user_choice = ""

#while loop is used to have the user keep on guessing until the same number is correctly guessed.
while user_choice != computer_choice:
    
    #Input for user
    user_choice = int(input("Guess a number between 1 to 100: "))

    #If the input number is bigger than the computer's number, this message is printed.
    if user_choice > computer_choice:
        print("The number is too high. Try again.")
        attempts += 1

    #If the input number is smaller than the computer's number, this message is printed.
    if user_choice < computer_choice:
        print("The number is too low. Try again.")
        attempts += 1

    #If the input number and the computer's number are equal, the user correctly guessed the answer and the number of attempts is printed.
    if user_choice == computer_choice:
        #Output
        print("You guessed the number!")
        print(f"It took you {attempts} attempts to guess correctly.")
        
