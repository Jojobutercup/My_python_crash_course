#!/bin/usr/env python3
""" multiple of 10 """
query = "lets check if your number is a multiple of 10"
query += "\nplease input your number? "

input_number = input(query)
number = int(input_number)

if number % 10 == 0:
    print(f"\t{number} if a multiple of 10")
else:
    print(f"\t{number} is not a multiple of 10, log another number")
