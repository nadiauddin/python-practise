### 01/04/2020
### Nadia Uddin
### Returning a value in a function

# Processes data to return a value or set of values - takes value from inside function

# e.g. 1: returning a name
def formatted_name(first_name, last_name):
    """Return a formatted name"""
    full_name = first_name + " " + last_name
    return full_name.title()

teacher = formatted_name('nadia', 'uddin')
print(teacher)

# e.g. 2: returning a username
# .strip() strips any white space that may be used
def get_formatted_username(email_address):
    """Return a formatted username"""
    username = email_address.strip()
    return username
user = get_formatted_username('nadiauddin@gmail.com')
print(user)