#Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#Make a list of five or more usernames called current_users.
#Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list

current_users = ['josephine', 'tinuade', 'chinemerem', 'damilola', 'pinnacle']
new_users = ['tinuade', 'tosin', 'sharon', 'Pinnnacle']
#Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
for new_user in new_users:
#Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, suc
    if new_user in current_users:
        print("you will need to enter a new username")
    else:
        print("username is available, please proceed")
print("\nUsers online")

