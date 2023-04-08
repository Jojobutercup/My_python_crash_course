#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
#Use insert() to add one new guest to the beginning of your list
#Use insert() to add one new guest to the middle of your list
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list
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
print(f"{Guest6.title()}, you are invited to dinner at my house this coming holiday.")
print(f"{Guest7.title()}, you are invited to dinner at my house this coming holiday.")
