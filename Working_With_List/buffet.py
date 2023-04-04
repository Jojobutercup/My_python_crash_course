# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple Use a for loop to print each food the restaurant offers.Try to modify one of the items, and make sure that Python rejects the change The restaurant changes its menu, replacing two of the items with differen foods. Add a line that rewrites the tuple, and then use a for loop to printfoods. Add a line that rewrites the tuple, and then use a for loop to print
menus = ('salad', 'rice', 'snacks', 'beef','garri')
print("we offer these five basic foods:")
for menu in menus:
    print(menu)
menus[0] = 'spaghetti'
print(menus)
menus = ('salad', 'rice', 'snacks', 'beef','garri', 'spaghetti', 'beans')
print("\n, This is the modified list;")
for menu in menus:
    print(menu)
