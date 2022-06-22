#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Create an empty dictionary to store pairs of values
dictionary = {}

#Inputs for name and age
name_input = input("Enter a name: ")
age_input = input("Enter an age of this person: ")

#Adds values to dictionary
dictionary.update({name_input:age_input})

#While loop continues until user inputs "stop"
while name_input.lower() != "stop":
    name_input = input("Enter a name (or 'stop' to stop): ")
    if name_input.lower() != "stop":
        age_input = input("Enter an age of this person: ")
        dictionary.update({name_input:age_input})

    elif name_input.lower() == "stop":
        break

#The values function is used to return the values from the dictionary
all_values = dictionary.values()
#The max function is used to return the item with the highest value
max_value = max(all_values)
search_key=max_value

#Output
for name_input in dictionary:
    if dictionary[name_input] == search_key:
        print(f"{name_input} is the oldest person in the group.")
    
