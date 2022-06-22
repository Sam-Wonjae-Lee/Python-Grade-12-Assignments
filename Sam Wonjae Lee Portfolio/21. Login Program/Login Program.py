#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Number of attempts
attempts = 3

#Login Dictionary
dictionary = {"Lee":"349740803", "Etwaroo": "123456789", "Foti": "987654321", "Papadatos": "543219876", "Tremblay":"9058899696"}

#Verified Flag
verified_flag = []

#Append "False" to verified flag
for i in range(len(dictionary)):
    verified_flag.append("False")

#Inputs
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

#While loop runs until user runs out of attempts
while attempts != 0:
    #Check if inputs are in dictionary
    if username_input in dictionary:
        if dictionary[username_input] == password_input:
            #Output
            print(f"Welcome {username_input}.")

            #Replace an index from verified flag to "True" based on which username and password is successful
            verified_flag[list(dictionary).index(username_input)] = "True"
            break

    #When inputs are not in dictionary
    if username_input not in dictionary or dictionary[username_input] != password_input:
        attempts -= 1
        print(f"User or password is wrong. You have {attempts} more attempts.")
        

    #When attempts run out
    if attempts == 0:
        print("You've ran out of attempts.")
        break

    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
        
