# An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.
from Restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(self.name.title() + " has flavors: ")
        for flavor in flavors:
            print(flavor)

flavors = ['american', 'asians']
ice_cream_stand = IceCreamStand("restuant1", "cuisine_type1", flavors)
ice_cream_stand.display_flavors()
    
