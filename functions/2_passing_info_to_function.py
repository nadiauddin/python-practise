### 19/02/2020
### Nadia Uddin
### Passing information to a function

#username in brackets is called a parameter
# a function can have multiple parameters
def hello_world(username):
    """Showing a username"""
    print("Hello " + username.title() + "!")

# what's in the brackets here is called the argument
# if there's only one parameter there needs to only be one argument
hello_world('nadia')