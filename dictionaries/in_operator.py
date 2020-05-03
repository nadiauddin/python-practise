### 17/02/2020
### Nadia Uddin
### Python's IN operator - used to check if a key-value pair exists

# Create a dictionary of terms
terms = {'variable' : 'Represents or refers to a value stored in memory', 'string' : 'A sequence of characters'}

if 'float' in terms:
    print("I know what a float is.")
else: print("I don't know what a float is.")

# Now starting with an empty dictionary

terms = {}

terms['variable'] = 'Represents or refers to a value stored in memory.'
terms['integer'] = 'A whole number.'

print(terms['variable'])
print(terms['integer'])