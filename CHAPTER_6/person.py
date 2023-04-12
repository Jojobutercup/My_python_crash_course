#Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
my_bestfriend = {'first_name': 'adetola', 'last_name': 'George', 'age': 25, 'city': 'lagos'}
firstname = my_bestfriend['first_name'].title()
secondname = my_bestfriend['last_name'].title()
bf_age = my_bestfriend['age']
place = my_bestfriend['city'].title()
print(f"my bestfriend names is {firstname} {secondname}, bestie's age is {bf_age}, bestie lives in {place}")
