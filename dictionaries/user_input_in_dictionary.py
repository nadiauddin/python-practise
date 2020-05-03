### 19/02/2020
### Nadia Uddin
### Adding user input to a dictionary

# property renting program
# Creating an empty dictionary
rental_properties = {}

# Set a flag to indicate we are taking applications
rental_open = True

while rental_open:
    #prompt users for their name and address
    username = input("\nWhat is your name? ")
    rental_property = input("\nWhat is the address of the property that you have to rent? ")

# Store the responses in the dictionary
    rental_properties[username] = rental_property

# Ask if the user knows someone else looking to rent
    repeat = input("\nDo you know anyone else who might be interested in renting their property? ")
    if repeat == 'no':
        rental_open = False

    # Adding property is complete

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent.")