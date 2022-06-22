#Sam Wonjae Lee


name = "Wonjae"
print("Hello " + name "!")

while True:
    num_a = int(input("Enter a value for a: "))
    num_b = int(input("Enter a value for b: "))  
    num_sum = num_a + num_b
    
    print(f'The sum of a and b is: {num_sum}')
    
    choice = input("Would you like to do this again (yes/no): ")
    if choice == "no":
        print("Goodbye.")
        break

