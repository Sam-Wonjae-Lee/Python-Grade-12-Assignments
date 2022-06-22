#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Start time leaving house, 6:52 am, in minutes
StartTime = 412

EasyPace = 8 + 15/60
Tempo = 7 + 12/60

#EasyPace is multiplied by 2 since he travels 1 kilometre twice at an easy pace
#Tempo is multiplied by 3 since he travels 3 kilometres at tempo
TotalTimeMinutes = EasyPace * 2 + Tempo * 3

FinalTime = StartTime + TotalTimeMinutes

#Use both division and modulus operators to find hour and minutes values for output
hour = int(FinalTime/60)
minutes = int(FinalTime % 60)

#Output
print(f"The end time is {hour}:{minutes}")
