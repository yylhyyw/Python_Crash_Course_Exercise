#  Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.


# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.


def make_album(artist, title, tracks_number=""):
    if tracks_number:
        return {"artist" : artist.title(), "title": title.title(), "tracks_number": tracks_number}
    else:
        return {"artist" : artist.title(), "title": title.title()}

album1 = make_album("Michael Jackson", "Dangerous", 8)
album2 = make_album("Beatles", "Let it be", 10)
album3 = make_album("Coldplay", "Everyday Life")

album_list = [album1, album2, album3]
for album in album_list:
        if not "tracks_number" in album.keys():
            print("This album is make by " + album["artist"] + " and the name is " + album["title"] + ".")
        else:
            print("This album is make by " + album["artist"] + " and the name is " + album["title"] + " and the number of tracks are " + str(album["tracks_number"]) + ".")
