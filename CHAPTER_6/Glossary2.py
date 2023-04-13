#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output
Glossary = {
        'variable': 'is a value place holder',
        'list': 'a group of items in a square bracket',
        'tuple': 'a list with permanent values',
        'if statement': 'is used to test for conditions, which results to either True or False test',
        'for loop': 'goes through items in a list, dictionarie',
        'items': 'values that makes up a tuple, list, dictionary',
        'methods': 'used for manipulating list, strings, dictionaries etc',
        'function': 'performs an operation/task',
        'key': 'used to access a value in a dictionary',
        'print': 'shows desired result to the screen',
        }
for key, value in Glossary.items():
        print(f"{key.title()}: \n{value}\n" )
