people_favorite_numbers = {"bill" : [10,11],
                            "john": [11, 12],
                            "mike": [12, 13],
                            "jack": [13, 14],
                            "dennis": [14, 15]}

for key, value in people_favorite_numbers.items():
    print(key + ' has the favorite number: ')
    for number in value:
        print(number)