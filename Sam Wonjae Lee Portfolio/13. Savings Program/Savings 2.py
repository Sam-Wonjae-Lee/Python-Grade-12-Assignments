#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#While loop is used to prevent invalid inputs
while True:
    #Check for errors
    try:
        #Input for how much you can save towards a goal
        goal = float(input("Enter the amount of money that you would like to save? "))
    except ValueError:
        print("That input is invalid. Please try again.")
        continue
    #Prints message if input is negative
    if goal < 0:
        print("Do not enter a negative number. Please try again.")
    else:
        break

#Input for period 
period = input("Enter the period of how often you are planning to save money (day/week/month/year): ").lower()

#While loop to prevent invalid inputs that does not include day, week, month and year
while period != "day" and period != "week" and period != "month" and period != "year":
    print("Please enter a proper period.")
    period = input("Enter the period of how often you are planning to save money (day/week/month/year): ").lower()

#While loop is used to prevent invalid inputs
while True:
    #Check for errors
    try:
        #Input for how much you can save each period
        payment = float(input(f"Enter the amount you want to save each {period}: "))
    except ValueError:
        print("That input is invalid. Please try again.")
        continue
    #Prints message if input is negative or zero
    if payment <= 0:
        print("Do not enter a zero or negative number. Please try again.")
    else:
        break

#Calculation for how long it will take to reach the goal    
time = goal/payment
time = "{:0.2f}".format(time)

#Output
print(f"It will take {time} more payments/{period}s to reach your goal.")
