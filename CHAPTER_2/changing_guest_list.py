#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting
#Print a second set of invitation messages, one for each person who is stil in your lis
Guest = ['damilola', 'sharon', 'tosin', 'mitchell']
Guest1 = Guest[0]
Guest2 = Guest[1]
Guest3 = Guest[2]
Guest4 = Guest[3]
print(f"{Guest4.title()}, will no longer be joining the party due to marital reasons.")
Guest[-1] = 'timi'
Guest4 = Guest[-1]

print(f"Hello {Guest4.title()},\n\t you are now my newly invited guest, for my dinner party at my house this coming holiday, \nplease relate any reasons for not coming, to me.\n")

print(f"Good day {Guest1.title()}, \n\tyou are still invited to dinner at my house this coming holiday.\n please relate any reasons for not coming to me.\n")

print(f"Good day {Guest2.title()},\n\t you are still invited to dinner at my house this coming holiday. \nplease relate any reasons for not coming to me.\n")

print(f"Good day{Guest3.title()}, \n\tyou are still invited to dinner at my house this coming holiday. \nplease relate any reasons for not coming to me.\n")
