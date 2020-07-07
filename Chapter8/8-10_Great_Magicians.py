# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. 
# Call show_magicians() to
# see that the list has actually been modified.


magicians = ['magician1', 'magician2', 'magician3']

def make_great(magicians):
    for i in range(0,3):
        magicians[i] = "Greate " + magicians[i]
def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is in the magician list.")


make_great(magicians)
show_magicians(magicians)