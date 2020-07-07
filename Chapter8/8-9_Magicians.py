# Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list

magicians = ['magician1', 'magician2', 'magician3']

def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is in the magician list.")

show_magicians(magicians)