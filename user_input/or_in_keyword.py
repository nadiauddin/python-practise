### 17/02/2020
### Nadia Uddin
### Using the OR keyword to check values in a list

# Name registered
registered_names = ['nadia', 'saira', 'salma', 'nabeelah']

username = input("Please enter the username you would like to use. ")

# Check to see if username is already taken
if username in registered_names:
    print("Sorry, username already taken")
else:
    print("This username is available.")

# PYTHON'S NOT IN KEYWORD
# Checking when a value is not in a list e.g. for admin vs normal users

admin_users = ['nadia', 'saira']

# Ask for username
username = input("Please enter your username. ")

# Checking if username is in list of admins
if username not in admin_users:
    print("You do not have access.")
else: print("Access granted.")