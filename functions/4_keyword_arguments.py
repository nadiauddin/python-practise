### 30/03/2020
### Nadia Uddin
### Keyword arguments

# They are name-value pairs that are passed to arguments
# Directly associate the name and value within the argument
# Keyword order doesn't matter

# Create a function
def book_description(book_type, author):
    """Display book information"""
    print("\nThis is a " + book_type + " book.")
    print("The author is " + author.title() + ".")

book_description(book_type='non-fiction', author='brad stone')