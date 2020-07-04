favorite_pizza = ['Chicago Pizza', 'Detroit Pizza', 'Greek Pizza']

for pizza in favorite_pizza:
    print('I like ' + pizza)

print("I really don't love pizaa!")

friend_pizzas = favorite_pizza[:]

# add a new pizza to the orginial list
favorite_pizza.append('New York Pizza')

# add a different pizza to friend list
friend_pizzas.append('Boston Pizza')

# print to show different lists:
print('My Favorite pizzas are: ')
for pizza in favorite_pizza:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)