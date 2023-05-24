prompt = "if you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"\nHello {name}!")

age = input("How old are you: ")
age = int(age)
if age > 48:
    print("You are old enough to smoke")
else:
    print("You are too young to smoke")
