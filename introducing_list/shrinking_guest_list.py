#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests
#Add a new line that prints a message saying that you can invite only two people for dinner
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner
# Print a message to each of the two people still on your list, letting them know they’re still invited
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program
Guest = ['damilola', 'sharon', 'tosin', 'mitchell']
Guest1 = Guest[0]
Guest2 = Guest[1]
Guest3 = Guest[2]
Guest4 = Guest[3]
print(Guest)
Guest.insert(0, 'Adetola')
Guest.insert(3, 'juwon')
Guest6 = Guest.append('timi')
print(Guest)
Guest1 = Guest[0]
Guest2 = Guest[1]
Guest3 = Guest[2]
Guest4 = Guest[3]
Guest5 = Guest[4]
Guest6 = Guest[5]
Guest7 = Guest[6]
print(f"{Guest1.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest4.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest5.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest2.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest3.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest6.title()}, you are invited to dinner at my house this coming holiday ")
new_message = ("I just found out that my reserved dinner table won't be available at the time of the dinner.\n I am left with the option of only inviting two people for dinner. \nPLEASE BARE WIT ME!")
print(new_message)
new_list1 = Guest.pop(6)
new_list2 = Guest.pop(5)
new_list3 = Guest.pop(4)
new_list4 = Guest.pop(3)
new_list5 = Guest.pop(2)
print(f"{new_list1.title()}, my sincere apologies goes to you,  as you are no longer invited to my dinner party. \nDue to technical issues above my control, I just found out that my new dinner table won’t arrive in time for the dinner. \n IF YOU DEY VEX, YOUR PAPA!\n")
print(f"{new_list2.title()}, my sincere apologies goes to you,  as you are no longer invited to my dinner party. \nDue to technical issues above my control, I just found out that my new dinner table won’t arrive in time for the dinner. \n IF YOU DEY VEX, YOUR PAPA!\n")
print(f"{new_list3.title()}, my sincere apologies goes to you,  as you are no longer invited to my dinner party. \nDue to technical issues above my control, I just found out that my new dinner table won’t arrive in time for the dinner. \n IF YOU DEY VEX, YOUR PAPA!\n")
print(f"{new_list4.title()}, my sincere apologies goes to you,  as you are no longer invited to my dinner party. \nDue to technical issues above my control, I just found out that my new dinner table won’t arrive in time for the dinner. \n IF YOU DEY VEX, YOUR PAPA!\n")
print(f"{new_list5.title()}, my sincere apologies goes to you,  as you are no longer invited to my dinner party. \nDue to technical issues above my control, I just found out that my new dinner table won’t arrive in time for the dinner. \n IF YOU DEY VEX, YOUR PAPA!\n")
print(Guest)
print(f"{Guest1.title()}, You are till invited to my dinner party, Thank you for letting out time.")
print(f"{Guest2.title()}, You are till invited to my dinner party, Thank you for letting out time.")
