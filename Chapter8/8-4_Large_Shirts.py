# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size="medium", message="I Love Python!"):
    print("This T-Shirt has size of " + str(size) + " and a message " + "'" + message.title() + "'" + ' that printed on it.')

# call function with default values
make_shirt()
# call funcation with user's values
make_shirt(8, "Hello, World!")