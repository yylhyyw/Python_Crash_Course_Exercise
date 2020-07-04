languages = ['Chinese', 'English']

print(languages)

# append one at the end of the list
languages.append('Spanish')
print(languages)

# pop one of the list
poped_language = languages.pop()
print('poped language is ' + poped_language)
print(languages)

# insert one at the beginning of the list
languages.insert(0, "Spanish")
print(languages)

# del the first language
del languages[0]
print(languages)

# remove Englisg from the list
languages.remove('English')
print(languages)