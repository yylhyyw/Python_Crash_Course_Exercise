current_users = ['bill', 'mike', 'jack', 'john', 'dennis']
# convert each users in current users to lowercase
current_users = [user.lower() for user in current_users]

new_users = ['bilL', 'JACk', 'emily', 'clara', 'cory']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ' is existed, you need to enter a new username.')
    else:
        print('the username is available!')