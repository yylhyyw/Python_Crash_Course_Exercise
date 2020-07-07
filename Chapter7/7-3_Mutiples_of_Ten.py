#  Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("please enter a number, and I will tell you weather" + 
                "the number if a multiple of 10 or not")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")