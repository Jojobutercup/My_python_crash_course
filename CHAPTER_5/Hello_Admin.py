#Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user
users = ['damilola', 'oluwajuwon', 'josephine', 'admin']
for user in users:
#If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
    if user == 'admin':
        print(f"Hello {user.title()}, would ypu like to see a status report?")
#Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again
    else:
        print(f"Hello {user.title()}, thank you for logging in again")
print("\nAll members present")
