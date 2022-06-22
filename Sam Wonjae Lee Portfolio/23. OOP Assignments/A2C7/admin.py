#Sam Wonjae Lee
from user import User


class Privileges():
    privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Prints privileges"""
        print("This user has the following privileges: ", *(self.privileges), sep="\n")

class Admin(User):
    privileges = Privileges()
