#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Inputs for principal, rate and year
principal = float(input("What is the initial principal amount? "))
rate = float(input("What is the interest rate? "))
year = int(input("What is the number of years? "))

#Variable is used to set up while loop
a = 1

#While loop is used to calulate the interest for each year until the last year
while a != year + 1:

    #Principal Formula 
    principal = principal * (1 + rate)
    
    #Rounding up to 2 decimals and output
    print(str(a), "{:0.2f}".format(principal))

    #Increases variable by one for the loop to prepare the end for the last year
    a = a + 1
