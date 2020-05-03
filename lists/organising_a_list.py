# 4//02/2020
# Author: Nadia Uddin
# Organising a list

# creating a list of months and sorting it alphabetically
birthday_months = ['january', 'february', 'october', 'november']
birthday_months.sort()
print(birthday_months)

# using reverse alphabetical order with reverse sort method
birthday_months = ['january', 'february', 'october', 'november']

birthday_months.sort(reverse=True)
print(birthday_months)


# once a list has been organised in a specific way
# you can't go back to the original way the list was written
# but you can temporarily organise a list using the sorted method
birthday_months = ['january', 'february', 'october', 'november']
print(sorted(birthday_months))
print(birthday_months)

# .reverse() is the list exactly in reverse order
birthday_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

birthday_days.reverse()
print(birthday_days)

# HOW TO COUNT THE NUMBER OF ITEMS/LENGTH IN A LIST
# list of days of the week
birthday_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

print(len(birthday_days))