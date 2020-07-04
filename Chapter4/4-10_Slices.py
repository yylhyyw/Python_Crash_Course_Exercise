threes = list(range(3,31,3))
for number in threes:
    print(number)

# first three in the list:
print(threes[:3])

# three from the middle of the list:
print(threes[len(threes)//2:len(threes)//2+3])

# last three from the list:
print(threes[-3:])