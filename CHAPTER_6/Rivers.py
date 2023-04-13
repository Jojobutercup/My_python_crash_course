#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
major_rivers = {
	'nile': 'egypt',
	'congo': 'congo',
	'zambezi': 'zambia'
	}
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt
for river, country in major_rivers.items():
	print(f"The river {river.title()} runs through {country.title()}")
#Use a loop to print the name of each river included in the dictionary.
for rivers in major_rivers.keys():
	print('we have:')
	print(f"{rivers.title()}")
#Use a loop to print the name of each country included in the dictionary
for countries in major_rivers.value():
	print('This is the country:')
	print(f"{countries}")
