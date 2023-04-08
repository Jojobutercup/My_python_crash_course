#Lets test for equality with strings
car = 'audi'
print(car == 'subaru')

#lets test for inequality with strings
house = 'duplex'
print(house != 'penthouse')

#lets test if a name in upper case will be equal to the same name in lower case
car = 'top'
print(car == 'Top')

#lets test a number using equality
age = 9
print(age == 18)

#lets test a number using inequality 
age = 23
print(age != 23)

#lets test number is graeter than another number
weight = 123
print(weight > 130)

#lets test a number is less than another number
height = 6
print(height < 12)

#lets test a number is greater than or equals to another number
age = 73
print(age >= 60)

#lets test a number is less than or equals to aother number
serial_number = 1298
print(serial_number <= 2000)

sibling_0 = 18
sibling_1 = 21
#test the age of this siblings, to see which family qualifies for the examination, requirements are; every family should be above ages 20
print(sibling_0 <= 20 and sibling_1 <= 20)

#a company wants to pick who to employ between this two gradaute, part of the requirements are be above the ages of 20
job_aspirant_1 = 24
job_aspirant_2 = 17
print(job_aspirant_1 <= 20 or job_aspirant_2<= 20)

#lets test if an item is in a list for shopping
shopping_lists = ['milk', 'milo', 'cheese', 'noodles', 'full cream']
print(shopping_lists == 'noodles')

#lets test if an item is not in a list for shopping
shopping_lists = ['milk', 'milo', 'cheese', 'noodles', 'full cream']
print(shopping_lists != 'garri')
