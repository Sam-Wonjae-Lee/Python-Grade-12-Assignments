#Sam Wonjae Lee

#Set variable to store my name
name = "Sam"
#Friendly Message
print("Hello " + name + "!\n")

class User: 
    def __init__(self, first_name, last_name, student_id, gender):
        """Used to assign values for first name, last name, student id and gender"""
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Prints summary of user information"""
        print(f"\nThe user's name is {self.first_name} {self.last_name}.")
        print(f"Their gender is {self.gender}.")
        print(f"Their student id is {self.student_id}.")
        
    def greet_user(self):
        """Greets user"""
        print(f"Hello {self.first_name}")

    def increment_login_attempts(self):
        """Increments login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts"""
        self.login_attempts = 0
    
class Privileges():
    privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Prints privileges"""
        print("This user has the following privileges: ", *(self.privileges), sep="\n")

class Admin(User):
    privileges = Privileges()

#User 1
user1 = Admin("Wonjae", "Lee", "349740803", "male")
user1.greet_user()
user1.describe_user()
print()

print("Making login attempts...")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The user has {user1.login_attempts} login attempts")
print("Resetting login attempts...")
user1.reset_login_attempts()
print(f"The user has {user1.login_attempts} login attempts\n")

user1.privileges.show_privileges()
print()

#User 2
user2 = User("Seungjae", "Lee", "349740902", "male")
user2.greet_user()
user2.describe_user()
print()

#User 3
user3 = User("Hengjing", "Zhang", "350219242", "male")
user3.greet_user()
user3.describe_user()


