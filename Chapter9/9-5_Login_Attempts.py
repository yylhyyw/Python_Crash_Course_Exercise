# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User():
    
    def __init__(self, first_name, last_name, login_attempts, **others):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.others = others

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " has information: ")
        for other,value in self.others.items():
            print(other + ": " + str(value))
        print("login attempts: " + str(self.login_attempts))
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Test code
user1 = User("firstname1", "lastname1", 0, age=8, height=160)
user1.describe_user()

# increase login attempts by increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()

# increase login attempts by increment_login_attempts() again
user1.increment_login_attempts()
user1.describe_user()

# reset login attempts by reset_login_attempts()
user1.reset_login_attempts()
user1.describe_user()