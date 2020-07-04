favorite_languages = {'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")

names = ['jen', 'sarah', 'bill', 'jack']

for name in names:
    if name in favorite_languages.keys():
        print(name.title() + "'s favorite language is " + 
            language.title() + ".")
    else:
        print(name.title() + " please take a poll.")