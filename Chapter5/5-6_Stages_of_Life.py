person_age = 15

# if-elif-else chain
if person_age < 2:
    print('the person is a baby.')
elif 2 < person_age < 4:
    print('the person is a toddler.')
elif 4 < person_age < 13:
    print('the person is a kid.')
elif 13 < person_age < 20:
    print('the person is a teenager.')
elif 20 < person_age < 65:
    print('the person is an adult.')
else:
    print('the person is an elder.')