#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Number of days in each month that is not a leap year
number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Input
year_input = int(input("Enter a year: "))

#A year may be a leap year if it is divisible by 4
#Years that are divisible by 100 cannot be leap years unless they are also divisible by 400
if year_input % 4 == 0 and (year_input % 100 != 0 or year_input % 400 == 0):
    #Number of days in each month from a leap year
    number_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Step 1 - Print the list
print(f"The number of days in each month in the year {year_input} is {number_of_days}")

#Step 2 - Print the number of days in the month I was born which is February
print(f"The number of days in the month I was born in is {number_of_days[1]}")

#Step 3 - Print total number of days from the input year
print(f"The total number of days in the year {year_input} is {sum(number_of_days)}")

#Step 4 - Prints a list of the months of the summer which is during June to August
print(f"The number of days in the summer months in the year {year_input} is {number_of_days[5:8]}")

#Step 5 - Prints a list of the first three months
print(f"The number of the days in the first 3 months in the year {year_input} is {number_of_days[0:3]}")

#Step 6 - Prints a list of the last three months
print(f"The number of the days in the last 3 months in the year {year_input} is {number_of_days[-3:]}")

#Step 7 - Prints a list of the first three months and the last three months of the year which is Jan. to March and Oct. to Dec.
FirstAndLastMonths = number_of_days[0:3] + number_of_days[-3:]
print(f"The number of the days in the first 3 months and the last 3 months is {FirstAndLastMonths}")
