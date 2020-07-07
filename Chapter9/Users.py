# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


class User():
    
    def __init__(self, first_name, last_name, **others):
        self.first_name = first_name
        self.last_name = last_name
        self.others = others

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " has information: ")
        for other,value in self.others.items():
            print(other + ": " + str(value))

# test code
user1 = User("firstname1", "lastname1", age=8, height=160)
user2 = User("firstname2", "lastname2", age=10)
user3 = User("firstname3", "lastname3", age=15, height=180)
user1.describe_user()
user2.describe_user()
user3.describe_user()
