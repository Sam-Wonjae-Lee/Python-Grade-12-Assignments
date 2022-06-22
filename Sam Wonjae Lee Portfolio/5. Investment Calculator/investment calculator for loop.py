#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Inputs for principal, rate and year
principal = float(input("What is the initial principal amount? "))
rate = float(input("What is the interest rate? "))
year = int(input("What is the number of years? "))

#For loop is used to calculate the interest for each year until the last year
for a in range(1, year+1):

    #Principal Formula 
    principal = principal * (1 + rate)
    
    #Rounding up to 2 decimals and output
    print(a, "{:0.2f}".format(principal))
