pets = {'baoer': {'type': 'dog', 'owner': 'bill'},
        'mimi': {'type' : 'cat', 'owner': 'zion'}}

for key, value in pets.items():
    print(key + ' has: ')
    for key, value in value.items():
        print(key + ": " + value)