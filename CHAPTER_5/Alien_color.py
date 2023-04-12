#Turn your if-else chain from Alien_Colors.py into an if-elif-else chain.
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("5 coins added to cart")
elif 'yellow' in alien_color:
    print("nothing added")
else:
    print("nothing else to add")

alien_color = ['green', 'yellow', 'red']
if 'yellow' in alien_color:
    print("\n10 coins added to your cart")
elif 'red' in alien_color:
    print("nothing added")
else:
    print("nothing else to add")

alien_color = ['green', 'yellow', 'red']
if 'red' in alien_color:
    print("\n15 coins added to your cart")
elif 'green' in alien_color:
    print("nothing added")
else:
    print("nothing else to add")
