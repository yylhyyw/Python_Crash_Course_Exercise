#  Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.


print('deli has run out of pastrami!')

sandwich_orders = ['pastrami sandwich', 'egg sandwich', 'pastrami sandwich', 'beef sandwich', 
                    'chicken sandwich', 'pastrami sandwich']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if 'pastrami' in sandwich:
        print(sandwich + ' can not be made because the deli has run out of pastrami')
        continue
    finished_sandwiches.append(sandwich)
    print(sandwich + ' has finished!')

for sandwich in finished_sandwiches:
    print(sandwich + ' is finished!')
