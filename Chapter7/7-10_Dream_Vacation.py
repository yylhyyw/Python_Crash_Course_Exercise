# Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

name_message = "What's your name?"
name_message = "\nuse 'quit' to end the counting."
place_message = "If you could visit one place in the world, where would you go?"
place_message += "\nuse 'quit' to end the counting."

# dream vacation dictionary
dream_vacation = {}
poll = {}

while True:
    name = input(name_message)
    if name == 'quit':
        break
    place = input(place_message)
    if place == 'quit':
        break
    dream_vacation[name] = place

for name,place in dream_vacation.items():
    print(name + "'s dream vacation is " + place + '.')
    if place in poll.keys():
        poll[place] += 1
    else:
        poll[place] = 0

for place, votes in poll.items():
    print(place + ' has votes ' + str(votes))




