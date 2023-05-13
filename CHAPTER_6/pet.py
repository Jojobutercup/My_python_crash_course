#!/usr/bin/env python3

""" each dictionary represents a different pet"""
dogs = {
        'bread1': 'german sherpherd',
        'owner1': 'sando',
        'bread2': 'chow chow',
        'owner2': 'praise',
        }
cats = {
        'breed1': 'persian',
        'owner1': 'uche',
        'breed2': 'siamese',
        'owner2': 'justin',
        }
Birds = {
        'breed1': 'budgerigar',
        'owner1': 'jojo',
        'breed2': 'cockatiel',
        'owner2': 'daniella',
        }
reptiles = {
        'breed1': 'ball python',
        'owner1': 'witched',
        'breed2': 'bearded dragon',
        'owner2': 'timi',
        }
amphibians = {
        'breed1': 'yellow and black dart frog',
        'owner1': 'tobi',
        'breed2': 'red-eyed tree frog',
        'owner2': 'jesuni',
        }
pets = [dogs, cats, Birds, reptiles, amphibians]

for owned_pets in pets:
    print(owned_pets)


