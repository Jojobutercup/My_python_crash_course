#
pizzas = ['pepperoni', 'meatpie', 'suya']
friend_pizzas = pizzas[:]
print(pizzas)
print(friend_pizzas)
pizzas.append('plain')
friend_pizzas.append('spicy')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

