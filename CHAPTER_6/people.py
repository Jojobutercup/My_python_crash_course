#!/usr/bin/python3
""" two new dictionaries representing different people"""
friend_1 = {'first_name': 'adetola', 'last_name': 'George', 'age': 25, 'city': 'lagos'}
friend_2 = {'first_name': 'sharon', 'last_name': 'olatunji', 'age': 20, 'city': 'ondo'}
friend_3 = {'first_name': 'juwon', 'last_name': 'oladiti', 'age': 50, 'city': 'lagos'}

"""stored all three dictionaries in a list called people"""
people = [friend_1, friend_2, friend_3]
for person in people:
    print(person)
