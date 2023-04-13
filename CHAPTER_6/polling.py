#Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
        }
people = ['phil', 'sarah', 'festus', 'sharon']
#Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll
for persons in favorite_languages.keys():
    print(persons.title())

    if persons in favorite_languages:
        print("\tyou have taken the poll")
    else:
        print("kindly take the poll")
