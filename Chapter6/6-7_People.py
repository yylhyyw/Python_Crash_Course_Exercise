person = {
    "aeinstein": {"first_name" : "Albert", 
        "last_name": "Einstein",
        "age": "999",
        "city": "Berlin"},
    "brussell":
        {"first_name" : "Bertrand", 
        "last_name": "Russell",
        "age": "999",
        "city": "Cambriage"},
        }

for key, value in person.items():
    print(key + ' has:')
    for key, value in value.items():
        print(key + ': ' + value)