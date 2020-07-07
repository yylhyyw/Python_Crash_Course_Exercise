# Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.


prompt = "\nTell me a pizza topping:"
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    topping = input(prompt)
    
    if topping == "quit":
        break
    elif topping == "stop loop":
        active = False
    else:
        print("added " + topping + "!")