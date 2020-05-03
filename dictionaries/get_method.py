### 17/02/2020
### Nadia Uddin
### Using the get() method to retrieve a value from a dictionary

# safety net when you ask for key with no value

terms = {'integer' : 'A whole number'}

print(terms.get('integer', 'Not in the dictionary'))

print(terms.get('float', 'Not in the dictionary'))
