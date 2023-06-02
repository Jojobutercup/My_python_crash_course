#!/bin/usr/env python3
"""
loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value.
"""
prompt = "Welcome to Our Store"
prompt += "\nEnter 'quit' to complete order"
prompt += "\nEnter your pizza toppings: "

active = True
while active:
    pizza_toppings = input(prompt)
    if pizza_toppings.lower() == 'quit':
        break
    elif pizza_toppings.isdigit():
        continue
    else:
        print(f"{pizza_toppings.title()}, added to your Order")
        active = False
print("Thanks for shopping with us")
