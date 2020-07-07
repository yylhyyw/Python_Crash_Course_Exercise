# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " restaurant is a " + self.cuisine_type + " restaurant.")
    
    def open_restaurant(self):
        print(self.name.title() + " is open!")

# Test code
restaurant = Restaurant("restaurant1", "cuisine_type1")
print("created a restaurant called resturant1 and has type of cuisine_type1.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
