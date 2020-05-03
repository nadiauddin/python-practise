### 11/02/2020
### Nadia Uddin
### Branching is a condition to take over another
### Python's if statement

print("To continue, please log in.")

# Using the if password
password = input("Please enter your password. ")
if password == "nadia":
    print("Access granted.")
else: print("Incorrect password, please try again.")

# If statements are like tests and can be evaluated as true or false

my_birthday = "October"

if my_birthday != 'March':
    print("It's not your birthday.")

age = 23
my_age = int(input("How old are you? "))
if my_age <= 22:
        print("Sorry, no cake for you.")
else: print("You can have some cake.")