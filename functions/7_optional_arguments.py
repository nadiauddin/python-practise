### 01/04/2020
### Nadia Uddin
### Making arguments optional

# RECAP: Argument is what's contained in the bracket for values to be returned

# NOTE: middle name moved to the end and assigned a default value in the form of an empty string
def formatted_name(first_name, last_name, middle_name=''):
    """Returning a full name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
teacher = formatted_name('nadia', 'uddin', 'mossammet')
print(teacher)