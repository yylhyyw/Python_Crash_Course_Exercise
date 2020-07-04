usernames = ['admin', 'bill', 'jack', 'mike', 'john']

for user in usernames:
    if user == 'admin':
        print('Hello ' + user + ', would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again.')