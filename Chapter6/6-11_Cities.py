cities = {"beijing" : {"country" : "China",
                        "population": "21.54 million",
                        "fact": "Yet it’s known as much for modern architecture as its ancient sites such as the grand Forbidden City complex"},
        "london": {"country": "England", 
                    "popualtion": "8,908,081",
                    "fact": " the capital of England and the United Kingdom, is a 21st-century city with history stretching back to Roman times"},
        "berlin": {"country": "Germany",
                    "population": "3.769 million",
                    "fact": "Germany’s capital, dates to the 13th century. Reminders of the city's turbulent 20th-century history include its Holocaust memorial and the Berlin Wall's graffitied remains."}}


for key, value in cities.items():
    print(key + ' has: ')
    for key, value in value.items():
        print(key + ": " + value)