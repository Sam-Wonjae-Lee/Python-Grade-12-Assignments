#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Open and read the original text file
with open('ICS4UDesiderata.txt') as file_object:
    text_file = file_object.read()

#Replace <l> with new line and <p> with double new line
text_file = text_file.replace('<l>', '\n')
text_file = text_file.replace('<p>', '\n\n')

#Create a new text file with the new proper format
with open("SamLeeDesiderata.txt", 'w') as file_object:
    file_object.write(text_file)
