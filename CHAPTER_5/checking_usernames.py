#Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#Make a list of five or more usernames called current_users.
#Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list

current_users = ['josephine', 'tinuade', 'chinemerem', 'damilola', 'pinnacle']
new_users = ['tinuade', 'tosin', 'sharon', 'Pinnnacle']
for new_user in new_users:
    if new_user in current_users:
        print("you will need to enter a new username")
    else:
        print("username is available, please proceed")
print("\nUsers online")

