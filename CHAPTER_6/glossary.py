#Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values
Glossary = {
        'variable': 'is a name assigned to a value', 
        'list': 'a group of items in a square bracket', 
        'tuple': 'a list with permanent values', 
        'if statement': 'is used to test for conditions, which results to either True or False test', 
        'for loop': 'goes through items in a list'
        }
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output
print(f"Variable: \n{Glossary['variable']}" )
print(f"List: \n{Glossary['list']}")
print(f"Tuple: \n{Glossary['tuple']}")
print(f"If Statement: \n{Glossary['if statement']}")
print(f"For Loop:\n{Glossary['for loop']}")
