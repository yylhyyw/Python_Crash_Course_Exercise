#  Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop


def make_album():
    artist_message = "Enter album's artist: \n"
    title_message = "Enter album's title: \n"
    album_dictionary = {}

    while True:
        artist = input(artist_message)
        if artist == "quit":
            break
        title = input(title_message)
        if title == "quit":
            break
        album_dictionary["artist"] = artist.title()
        album_dictionary["title"] = title.title()
        print("This album is make by " + album_dictionary["artist"] + " and the name is " + album_dictionary["title"] + ".")

make_album()
