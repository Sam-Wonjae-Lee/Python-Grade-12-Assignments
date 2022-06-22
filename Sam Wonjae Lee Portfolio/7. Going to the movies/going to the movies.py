#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Input
name = input("What is your name? ").title()
age = int(input(f"Hello {name}! How old are you? "))

#If statements to determine ticket price and outputs
if age <0:
    print("Age cannot be negative. Try again!")
    
elif age < 3:
    print("The price of your ticket is $0.00.")

elif age <= 12 and 3<= age:
    print("The price of your ticket is $10.00.")

elif age >= 65:
    print("The price of your ticket is $15.00.")

else:
    print("The price of your ticket is $25.00.")
    

