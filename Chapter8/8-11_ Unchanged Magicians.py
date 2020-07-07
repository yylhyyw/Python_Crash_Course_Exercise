# Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.


magicians = ['magician1', 'magician2', 'magician3']

def make_great(magicians):
    temp_magicians = []
    for magician in magicians:
        temp_magicians.append("Greate " + magician)
    return temp_magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is in the magician list.")


new_magicians = make_great(magicians[:])
show_magicians(new_magicians)