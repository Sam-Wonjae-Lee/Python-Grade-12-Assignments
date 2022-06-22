#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Input for text file
data_file = input("Enter the name of the data file: ")
data_file = data_file + '.txt'

#Opens a text file for reading text
open_file = open(data_file, "r")

#Input for dates
day_date = input("For the date you care about, enter the day: ")
month_date = input("For the date you care about, enter the month: ")
year_date = input("For the date you care about, enter the year: ")

#Takes last 2 characters from year date input
year_date = year_date[-2:]

#Convert number values to month names to match text file
if month_date == "12":
    month_date = "Dec"

elif month_date == "1" or month_date == "01":
    month_date = "Jan"

elif month_date == "2" or month_date == "02":
    month_date = "Feb"

elif month_date == "3" or month_date == "03":
    month_date = "Mar"

elif month_date == "4" or month_date == "04":
    month_date = "Apr"

elif month_date == "5" or month_date == "05":
    month_date = "May"

elif month_date == "6" or month_date == "06":
    month_date = "Jun"

elif month_date == "7" or month_date == "07":
    month_date = "Jul"

elif month_date == "8" or month_date == "08":
    month_date = "Aug"

elif month_date == "9" or month_date == "09":
    month_date = "Sep"

elif month_date == "10":
    month_date = "Oct"

elif month_date == "11":
    month_date = "Nov"

#Full date
full_date = f"{day_date}-{month_date}-{year_date}"

#Check each line to see if the full date matches with any of the dates in DataFile1
for line in open_file:
    if full_date in line:
        weather_data = line
        #Use split function to split lines from each comma to seperate values
        weather_data = weather_data.split(",")
        #Output
        print('The low temperature was', weather_data[1], 'degrees celsius')
        print('The high temperature was', weather_data[2], 'degrees celsius')
        print('The average temperature was', weather_data[3], 'degrees celsius')
        open_file.close()
        break

else:
    print("Date was not found")
        
        

