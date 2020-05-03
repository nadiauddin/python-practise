### 17/02/2020
### Nadia Uddin
### Looping through a dictionary

birthday_months = {
    'nadia' : 'october',
    'nabeelah' : 'november',
    'saira' : 'september',
    'salma' : 'february',
}

print(birthday_months)

for key, value in birthday_months.items():
    print("\nName: " + key)
    print("Birthday month: " + value)

# Looping is possible thru: k-v pairs, just keys, or just values

# Looping through key-value pairs:
book_1 = {
    'name': 'elon musk',
    'author': 'ashlee vance',
    'price': 14.99,
    'publisher': 'virgin books'
}

print(book_1)

for key, value in book_1.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

# You will notice k-v pairs are not printed in the order they're stored