### 17/02/2020
### Nadia Uddin
### Other ways to loop through a dictionary

# No.1: Using the keys method
# When you don't need to use all the values in a dict

birthday_months = {
    'nadia': 'october',
    'saira': 'september',
    'nabeelah': 'november',
    'salma': 'february',
}

# Use .keys to just get the keys

for name in birthday_months.keys():
    print(name.title())

# Using the value method
for months in birthday_months.values():
    print(months.title())

# Using the set method - similar to list but each item in the set must be unique
# e.g. if two ppl had the same birthday month, the month would be printed just once

birthday_months2 = {
    'nadia': 'october',
    'amy': 'october',
    'nabeelah': 'november'
}
for months in set(birthday_months2.values()):
    print(months.title())
