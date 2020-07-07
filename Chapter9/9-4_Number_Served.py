# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
# day of business.

class Restaurant():
    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.name.title() + " restaurant is a " + self.cuisine_type + " restaurant " + "has number of served of " + str(self.number_served) + ".")
    
    def open_restaurant(self):
        print(self.name.title() + " is open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self):
        self.number_served += 1

# Test code
restaurant = Restaurant("restaurant1", "cuisine_type1")
restaurant.describe_restaurant()

# change number of served to 10
restaurant = Restaurant("restaurant1", "cuisine_type1", 10)
restaurant.describe_restaurant()

# use set method to change number of served
restaurant.set_number_served(15)
restaurant.describe_restaurant()

# use increase method to increase number of served
restaurant.increment_number_served()
restaurant.describe_restaurant()