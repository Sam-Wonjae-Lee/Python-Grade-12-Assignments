#Sam Wonjae Lee

name = str(input("What is your name? "))
age = int(input(f"Hello {name}! How old are you? "))
num_of_tickets = int(input("How many tickets do you want? "))

if age < 3:
    price = 0
    cost = price * num_of_tickets
    print(f"The price of your ticket is ${cost}")

elif age < 12 and 3<= age:
    price = 10
    cost = price * num_of_tickets
    print(f"The price of your ticket is ${cost}")

elif age >= 65:
    price = 15
    cost = price * num_of_tickets
    print(f"The price of your ticket is ${cost}")

else:
    price = 25
    cost = price * num_of_tickets
    print(f"The price of your ticket is ${cost}")
