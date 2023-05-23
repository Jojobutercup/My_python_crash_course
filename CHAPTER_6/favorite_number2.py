#1/usr/bin/env python3

favorite_number = {
    'oluwajuwon': [7, 46, 6],
    'osas': [3, 18, 10],
    'timi': [1, 17, 9],
    'dami': [77,7],
    'sharon': [8, 5],
    }
for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorite numbers:")
    for number in numbers:
        print(f"\t{number}")
