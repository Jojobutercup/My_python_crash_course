#Store the numbers 1 through 9 in a list 
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Loop through the list
for ordinal_number in ordinal_numbers:
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")
