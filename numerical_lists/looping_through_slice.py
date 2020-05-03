# 10/02/2020
# Nadia Uddin
# Looping through a slice

# This is used to make things easier and smoother
# looping through a slice with a for loop

names = ['nadia','salma','nabeelah','saira']
print("Here are the names of the first 3 registrations:")
for name in names[:3]:
    print(name.title())

print("Here are the names of the last 3 registrations:")
for name in names[2:]:
    print(name.title())

# COPYING A LIST
# This is to manipulate and edit list without changing original code
names = ['nadia','salma','nabeelah','saira']
first_names = names[:]
print(first_names)