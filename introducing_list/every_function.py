#Alist that uses all the function
market_list = ['fish', 'maggi', 'leaf', 'sugar', 'milk']
#my mum ask me what did i write as my third item on the list
print(f"the third item in my list is {market_list[2].title()}")
print(market_list)
#mum said, oh i forgot to add egg, please buy the eggs if there is money left
market_list.append('eggs')
print(market_list)
#oh i forgot mum said she wont be needing the fish instead i need beans for my practicals tommorow, \n let me replace the fish with the beans
market_list[0] = 'beans'
print(market_list)
#how about i buy a bottle of water for practicals tommorrow
market_list.insert(1, 'water')
print(f"mum i had to take a few extra tens of nairas to buy {market_list[0].title()} and {market_list[1].title()} that i need for school")
print(market_list)
#osahen told mum not to buy the sugar anymore because of the health hazard it could cause
del market_list[-3]
print(market_list)
#now mum wants osahen to tell me to remove the unhealthy food in the list and tell her what i removed 
removed_item = market_list.pop(-4)
print(f"osahen removed {removed_item.title()} from the list")
print(market_list)
#lets add items to the end of our list
market_list.append('berries')
market_list.insert(2, 'sparkling water')
market_list.append('vegetables')
market_list.insert(0,'tomatoes')
print(market_list)
#now, mum wants to remove berries because its quite expensive, but we dont know where it is on the list
item_to_be_removed = 'berries'
market_list.remove(item_to_be_removed)
print(f"the reason mum removed {item_to_be_removed.title()} is because she finds it unreasonably expensive in that market")
#mum wants the list arranged in alphabetical order, and then items should be bought from the end to the first, lets see how it wiill look first before making final adjustments
print("This is the sorted list: ")
print(sorted(market_list))
print("back to the origal list< since you confirme the lust can i permanently change it?")
print(market_list)
#lets see the list sorted temporarily in reverse alphabetical order
print(sorted(market_list, reverse = True))
#now mum wants the sorted marlet list, so we hurry up and start buying what we need alphabetically
print("this is the new sorted list")
market_list.sort()
print(market_list)
#lets reverse this list
market_list.reverse()
print(market_list)
#how many items do we have in our list?
print("the number of items in the list are: ")
print(len(market_list)) 
