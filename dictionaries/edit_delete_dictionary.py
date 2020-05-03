### 17/02/2020
### Nadia Uddin
### Editing and deleting values in a dictionary

# Wrong definition of integer
terms = {'integer' : 'Is a number that contains a decimal place.', 'string' : 'A sequence of characters.'}

# Correction overrides incorrect definition
terms['integer'] = 'A whole number.'

print(terms.get('integer'))

print(terms.get('string'))

# Use del to remove key-value pair
del terms['integer']
print(terms)