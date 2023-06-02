#!/bin/usr/env python3
"""
loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value.
"""
prompt = "Welcome to Our Store"
prompt += "\nEnter 'Exit' to complete order"
prompt += "\nEnter your pizza toppings: "

pizza_toppings = ""
while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    print(f"{pizza_toppings.title()}, added to your Order")
