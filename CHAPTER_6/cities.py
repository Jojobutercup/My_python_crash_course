#!/usr/bin/env python3

"""A dictionary called cities"""
cities = {
        'lagos': {
            'country': 'nigeria',
            'facts': 'lagos was a slave port for the british empire',
            'population': 15946000
            },

        'benin': {
            'country': 'nigeria',
            'facts': 'The benin kingdom which is one of the oldest and most developed states in the coastal hinterland of west Africa.\n\tThe british invaded their land for the desire for control over west Africa trades and territory',
            'population': 13031215,
            },

        'new york': {
            'country': 'USA',
            'facts': 'I no sabi their papa',
            'population': 14989
            },
        }
for city, informations in cities.items():
    print(f"{city.title()}:")
    if informations['country'].lower() == 'usa':
        city_info = f"{informations['country'].upper()}"
        facts = f"{informations['facts']}"
        population = f"{informations['population']}"
        print(f"\tThis city is present in {city_info}.\n\tFUNFACTS! about the city:{facts}.\n\t{city.title()} has a population density of: {population} people\n")
    else:
        city_info = f"{informations['country'].title()}"
        facts = f"{informations['facts']}"
        population = f"{informations['population']}"
        print(f"\tThis city is present in {city_info}.\n\tFUNFACTS! about the city:{facts}.\n\t{city.title()} has a population density of: {population} people\n")
