#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#My date of birth in US format (MM/DD/YYYY)
DOB_in_US_format = "02/20/2004"

#Selects year from index 6 to 9
year_date = DOB_in_US_format[6:10]

#Selects month from index 0 to 1
month_date = DOB_in_US_format[0:2]

#Selects day from index 3 to 4
day_date = DOB_in_US_format[3:5]

#Output - Canadian Format (YYYY-MM-DD)
print(f"{year_date}-{month_date}-{day_date}")


