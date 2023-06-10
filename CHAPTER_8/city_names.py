def city_country(city, country):
    """Displays a city and its country"""
    place = f"{city}, {country}"
    return place.title()

full_address = city_country('lagos', 'nigeria')
another_pair = city_country('kano', 'nigeria')
another_one = city_country('edo', 'nigeria')
print(f'"{full_address}"')
print(f'"{another_pair}"')
print(f'"{another_one}"')
