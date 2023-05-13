#!/usr/bin/env python3

""" Make a dictionary called favorite_places """
favorite_places = {
        'isioma': ['paris', 'japan', 'mauritania'],
        'tola': ['ghana', 'canada', 'nigeria'],
        'jojo': ['paris'],
        'cath': ['dubai', 'texas'],
        }
for key, value in favorite_places.items():
    print(f"{key.title()}'s favourite places includes:")
    for place in value:
        print(place)
