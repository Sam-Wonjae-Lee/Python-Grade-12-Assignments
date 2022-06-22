#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Input for period
period = input("Enter the period of how often you are planning to save money (day/week/month/year): ").lower()

#While loop to prevent invalid inputs
while period != "day" and period != "week" and period != "month" and period != "year":
    print("Please enter a proper period.")
    period = input("Enter the period of how often you are planning to save money (day/week/month/year): ").lower()      

#Input for amount of money you would like to save towards a goal
goal = input("Enter the amount of money that you would like to save? ")

#While loop to prevent invalid inputs
while goal.isnumeric() ==  False or goal == "0" or goal == 0:
    print("That input is invalid. Please try again.")
    goal = input("Enter the amount of money that you would like to save? ")
        
#Input for the amount of money to save each period
payment = input(f"Enter the amount you want to save each {period}: ")

#While loop to prevent invalid inputs
while goal.isnumeric() == False or goal == "0" or goal == 0:
    print("That input is invalid. Please try again.")
    payment = input(f"Enter the amount you want to save each {period}: ")

time = int(goal)/int(payment)

#Output
print(f"It will take {time} {period}s to reach your goal.")
        


    

    
