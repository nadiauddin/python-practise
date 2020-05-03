### 19/02/2020
### Nadia Uddin
### While loops in lists are so u can edit the list as you work through it
# Can't edit lists in for loops

# e.g. when you sign up for a mailing list you have to verify your email address
# Once the user has verified their email they must move from the unverified list of addresses to the verified list
# Use a while loop to do this

# List of unverified users

unconfirmed_users = ['nadia', 'nabeelah', 'saira', 'salma']

# An empty list to hold confirmed users

confirmed_users = []

# While loop will run as long as list of unconfirmed users still has values in it
#.pop() pops user from one variable to the other
# in this case it will basically rename an unconfirmed user as a current user
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
# Append means to add to this list. so the current user will be added to the confirmed user list ONE AT A TIME
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())