#Add an if test to hello_admin.py to make sure the list of users is not empty,  Add an if test to hello_admin.py to make sure the list of users is not empty 
#Remove all of the usernames from your list, and make sure the correct message is printed.
users = []
if users:
    for user in users:
        print(f"welcome {user.title()}, send a new message")
    print("meet friends online")
else:
    print("We need to find some users!")
