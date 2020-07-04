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


# Find a bigger dinner table
print('I find a bigger dinner table')

# insert at beginning of the list
guest_list.insert(0, 'Dennis')

# insert at the middle of the list
guest_list.insert(len(guest_list)//2, 'Payton')

# insert at the end of the list
guest_list.append('Clara')

#print new invitation messages:
for guest in guest_list:
    print(guest + ' I would like to invite you to my dinner.')

# I can only invite two guests
print('I can only invite two people for dinner.')

# pop until last 2 guests
while len(guest_list) > 2:
    poped_guest = guest_list.pop()
    print(poped_guest + " I'm sorry you can't invite you to the dinner.")

# for guest in guest_list:
#     if len(guest_list) > 2:
#         poped_guest = guest_list.pop()
#         print(poped_guest + " I'm sorry you can't invite you to the dinner.")

# print invitation message for last 2 guests then del each of them
while guest_list:
    print(guest_list[0] + ' I would like to invite you to my dinner.')
    del guest_list[0]

print(guest_list)