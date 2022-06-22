#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Inputs for user name
user_name = str(input("What is your name? "))
user_age = int(input("How old are you? "))
print(f"Hello {user_name}!")

#Inputs for each age group
kids = int(input("How many tickets for kids under 3 years old? "))
older_kids = int(input("How many tickets for kids aged 12 and under? "))
seniors = int(input("How many tickets for Seniors aged 65 years and older? "))
adults = int(input("How many tickets for Adults? "))

#Calculation for final price for all tickets
final_price = (kids * 0) + (older_kids * 10) + (seniors * 15) + (adults * 25)
final_price = format(final_price, "0.2f")

#Output
print(f"Please pay ${final_price}")
