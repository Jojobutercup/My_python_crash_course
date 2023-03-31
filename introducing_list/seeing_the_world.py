#Store the locations in a list. Make sure the list is not in alphabetical orde Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
#Show that your list is still in its original order by printing it again.
#Print the list to show that its order has changed.
location = ['oymyakon', 'pripyat', 'Snake island', 'kingston jamaica']
print(location)
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(location))
#Show that your list is still in its original order by printing it
print(location)
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(location, reverse = True))
#Show that your list is still in its original order by printing it again
print(location)
#Use reverse() to change the order of your list. Print the list to show that its order has changed
location.reverse()
print(location)
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order
location.reverse()
print(location)
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
location.sort()
print(location)
#Use sort() to change your list so it’s stored in reverse alphabeticalorder. Print the list to show that its order has changed
location.sort(reverse = True)
print(location)
