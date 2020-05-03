### 30/03/2020
### Nadia Uddin
### Positional arguments

# Positional arguments refer to the fact that the arguments within the bracket of the function
# must be in the correct position or they will be read in the wrong direction

# Creating our function
def book_description(book_type, author_name):
    """Display book information"""
    print("\nThis book is " + book_type + ".")
    print("The author of this book is " + author_name.title() + ".")

# items in the brackets below are called arguments
book_description('non-fiction', 'ashlee vance')

book_description('fiction', 'nadia uddin')
book_description('',' haruki marukami')