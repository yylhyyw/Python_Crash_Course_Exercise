# : Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. 
# As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nTell me a pizza topping:"
prompt += "\nEnter 'quit' to end the program."

topping = ""
while not topping == "quit":
    print("added " + topping + "!")
    topping = input(prompt)

