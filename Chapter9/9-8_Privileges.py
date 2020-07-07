#  Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.
from Users import User


class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("this user has privileges: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, privileges, **others):
        super().__init__(first_name, last_name, others = others)
        self.privileges = privileges


admin = Admin("firstname1", "lastname2", Privileges(["can add post", "can delete post", "can ban user"]), age=8)
admin.privileges.show_privileges()