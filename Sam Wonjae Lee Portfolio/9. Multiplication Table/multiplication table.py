#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!\n")

#For loop is used to receive the first set of values from 1 to 12
for i in range(1, 13):
    #Another for loop is used to receive the second set of values from 1 to 12
    for j in range(1, 13):
        #Output; both sets of values are multiplied to print multiplcation table for 1 to 12
        #\t is used to evenly seperate the numbers
        print(i*j, end="\t")
    #Starts on a new line after a row is finished
    print("\n")
