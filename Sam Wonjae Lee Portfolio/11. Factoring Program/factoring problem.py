#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Option to enter a number or quit program
num = input('Enter a number to factor (or "QUIT" to quit): ')

if num.upper() == "QUIT":
    print("Goodbye.")
    exit
        
else:
    #Input
    num = int(num)
    print(f"The factors of {num} are: ")

    #Create a list for factors
    factor_list = []

    #Check to see if the number is capable of being divided while leaving a remainder of 0
    #+1 is added to num so we can include numbers from 1 to the input
    for a in range(1, num+1):
        if num % a == 0:
            #Add factors to list
            factor_list.append(a)

    #Output; sep is used to seperate each item in the list
    # * asterisk is used to unpack objects which removes brackets from list when printing
    print(*factor_list, sep = ', ')
