birthday_months = ['spril', 'may', 'otober', 'august']
print(birthday_months)

# Use [index] after the name of the variable to rewrite it in case there's a spelling mistake

birthday_months[0] = 'april'
print(birthday_months)

birthday_months[2] = 'october'
print(birthday_months)

# Use .append to add an element to a list

birthday_months.append('june')
print(birthday_months)

# Lists can be empty but can still be edited

birthday_months = []
print(birthday_months)

# Use append to add an element to the end of a list

birthday_months.append('september')
print(birthday_months)

# Use the insert method to input an element before an existing element

birthday_months.insert(0, 'may')
print(birthday_months)

# Use del to delete an element from a list if you know its index (number position in the list)
del birthday_months[1]      # Index would be [1]
print(birthday_months)