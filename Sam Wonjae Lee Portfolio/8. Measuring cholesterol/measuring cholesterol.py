#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!")

#Inputs
HDL = int(input("What is your HDL level? "))
LDL = int(input("What is your LDL level? "))
TRI = int(input("What is your TRI level? "))

#Total cholesterol amount is the sum of HDL, LDL & one fifth of TRI
cholesterol = HDL + LDL + (TRI/5)

print(f"Your total cholesterol level is {cholesterol}")

#Outputs
#If all categories are good, it will print out "Cholesterol looks great!"
if LDL < 100 and HDL > 60 and TRI < 150 and cholesterol < 200:
    print("Cholesterol looks great!")

#If one of the categories is bad, it will print "Warning: Cholesterol looks bad!"
elif LDL > 130 or HDL < 50 or TRI > 200 or cholesterol > 240:
    print("Warning: Cholesterol looks bad!")

#Otherwise, if the categories do not fall into either outcome, "Borderline cholesterol problems" will be printed.   
else:
    print("Borderline cholesterol problems.")
