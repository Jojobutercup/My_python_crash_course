#!/bin/usr/env python3
"""Number of large tables available"""
question = "My Restaurants Invites you"
question += "\nHow many people are in your dinner group? "

number_present = input(question)
number = int(number_present)

if number >= 8:
    print("you’ll have to wait for a table")
else:
    print("Please book your table")
