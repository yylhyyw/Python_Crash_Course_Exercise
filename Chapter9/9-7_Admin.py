#  An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
from Users import User


class Admin(User):

    def __init__(self, first_name, last_name, privileges, **others):
        super().__init__(first_name, last_name, others = others)
        self.privileges = privileges

    def show_privileges(self):
        print(self.first_name.title() + " " + self.last_name.title() + " has privileges: ")
        for privilege in privileges:
            print(privilege)

# Test code
privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin("firstname1", "lastname1", privileges, age=8)
admin.show_privileges()