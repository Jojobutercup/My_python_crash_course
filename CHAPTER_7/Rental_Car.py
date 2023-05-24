#!/bin/usr/env python3
""" rental car """
query = "Welcome to Josephine's Car Rentals"
query += "\nWhat kind of car do you want to rent? "

answer = input(query)
print(f"Please hold on. A staff will get to you shortly, for the {answer.title()}")
