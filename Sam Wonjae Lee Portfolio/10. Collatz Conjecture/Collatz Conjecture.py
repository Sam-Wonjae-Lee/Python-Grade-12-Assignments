#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Input
num = int(input("Enter a number: "))

#Counter for number of steps
step = 0

if num <= 0:
    print("Number should be positive.")
    
elif num == 1:
    print("It took 0 steps to reach 1 from the starting number.")
    
else:
    #While loop is run until the number is eventually 1
    while num != 1:
        #Modulus operator is used to find even numbers by checking if the number has a remainder of 0 when dividing with 2
        if num % 2 == 0:
            #Even numbers are divided by 2 to get the next number
            num /= 2
            print(int(num))
            step += 1

            #Output: Final Number
            if num == 1:
                print(f"It took {step} steps to reach to 1 from the starting number.")

        else:
            #Odd numbers are multiplied by 3 and added by 1 to get the next number
            num = 3*num + 1
            print(int(num))
            step += 1

            #Output: Final Number
            if num == 1:
                print(f"It took {step} steps to reach to 1 from the starting number.")

        
