places = ['London', 'Bosotn', 'Beijing', 'DC', 'LA']

# print lists in original order
print(places)

# print sorted lists without modifify actual list
sorted_places = sorted(places)
print(sorted_places)

# print lists again
print(places)

# reverse list and print it
places.reverse()
print(places)

# reverse again and print
places.reverse()
print(places)

# use sort() to change list
places.sort()
print(places)

# use sort() and reverse
places.sort(reverse=True)
print(places)