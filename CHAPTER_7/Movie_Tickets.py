#!/bin/usr/env python3
"""
theater charges different ticket prices depending on
a person’s age.
"""
prompt = "Please login your age, to calculate your bill"
prompt += "\nYour age: "

active = True 
while active:
    age = input(prompt)
    age = int(age)

    if age <= 3:
        print("your ticket is free")
        active = False
    elif age <= 12:
        print("your ticket is $10")
        active = False
    elif age > 12:
        print("your ticket $15")
        active = False

        
