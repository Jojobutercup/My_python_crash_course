users = ['damilola', 'oluwajuwon', 'josephine', 'admin']
for user in users:
    if user == 'admin':
        print(f"Hello {user.title()}, would ypu like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again")
print("\nAll members present")
