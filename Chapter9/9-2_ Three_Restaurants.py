# Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " restaurant is a " + self.cuisine_type + " restaurant.")
    
    def open_restaurant(self):
        print(self.name.title() + " is open!")

# Test code
restaurant1 = Restaurant("restaurant1", "cuisine_type1")
restaurant2 = Restaurant("restaurant2", "cuisine_type2")
restaurant3 = Restaurant("restaurant3", "cuisine_type3")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()