# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
    print("This T-Shirt has size of " + str(size) + " and a message " + "'" + message.title() + "'" + ' that printed on it.')

# call function using positional arguments
make_shirt(8, "Hello, World!")

# call function using keyword arguments
make_shirt(message="Hello, World!", size=8)
