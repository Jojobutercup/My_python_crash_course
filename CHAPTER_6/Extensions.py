#!/usr/bin/python3
""" two new dictionaries representing different people"""
favorite_people = {

        'friend1': {
            'first_name': 'adetola',
            'last_name': 'George',
            'age': 25,
            'city': 'lagos',
            },

        'friend2': {
            'first_name': 'sharon',
            'last_name': 'olatunji',
            'age': 20,
            'city': 'ondo',
            },

        'friend3': {'first_name': 'juwon',
            'last_name': 'oladiti',
            'age': 50,
            'city': 'abuja',
            },
        }
'''stored all three dictionaries in a list called people'''
for friends, friends_info in favorite_people.items():
    print(f"{friends.title()}")

    fullname = f"{friends_info['first_name']} {friends_info['last_name']}"
    age = f"{friends_info['age']}"
    cities =  f"{friends_info['city']}"
    print(f"My friends ages {age} includes {fullname.title()}, {friends_info['first_name'].title()} stays in {cities.title()}")
