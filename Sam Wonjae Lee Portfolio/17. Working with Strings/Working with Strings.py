#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Set variables to store my student ID, first and last name
MyStudentID = "349-740-803"
MyName = "Sam Lee"

#Selects first name from index 0 to 2 
FirstName = MyName[0:3]
#Reverses last name then selects index 0 to 2
LastName = MyName[::-1]
LastName = LastName[0:3]
#Selects index 4 to 6 from student ID
MiddleDigits = MyStudentID[4:7]

Password = f"{FirstName}{MiddleDigits}{LastName}"

#Output
print(Password)
