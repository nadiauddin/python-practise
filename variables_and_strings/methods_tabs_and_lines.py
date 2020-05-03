# find method is the same as "cmd + "
# can be used to find and delete spam from inbox

my_book = "My favourite book is 'Elon Musk'.".find('book')

print(my_book)

subject = "$$$ Get Rich Quick $$$".find("$$$")
print(subject)

# lower method starts here
# used to put strings into lower case in case they have been input in another way

name = "NADIA UDDIN".lower()
print(name)

# replace method replaces a piece of a string with another piece

my_book = "My favourite book is 'Elom Musk'.".replace('Elom', 'Elon')
print(my_book)

# Strip method removes any blank space on the LHS/RHS of a string

address_101 = "101 Main Street Dublin"
print(address_101)

address_strip = "       102 Main Street     "
print(address_strip.lstrip())

# .lstrip() removes space on the LHS
# .rstrip() removes space on the RHS
# .strip() removes space on both sides

# adding white space

address = "101 main street \tDublin"
print(address.title())

address = "102 main street \nDublin"
print(address.title())