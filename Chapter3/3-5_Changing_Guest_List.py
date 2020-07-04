guest_list = ['Bill', 'Jack', 'Mike']
for guest in guest_list:
    print(guest + ' I would like to invite you to my dinner.')

# print Bill can't attend the dinner
print("Bill can't attend the dinner")

# replace bill to John
for guest in guest_list:
    if guest == "Bill":
        guest_list.remove('Bill')
        guest_list.append('John')

# print invitation again:
for guest in guest_list:
    print(guest + ' I would like to invite you to my dinner.')