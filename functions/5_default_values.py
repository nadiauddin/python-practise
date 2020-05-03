### 30/03/2020
### Nadia Uddin
### Default values

# uses default value unless argument is specified

def book_description(author_name, book_type="non-fiction"):
    """Displaying book information"""
    print("\nThis is a " + book_type + " book.")
    print("The author is " + author_name.title() + ".")

# Don't need to put in book type argument because default has already been written
book_description('ashlee vance')

# The order of author name and book type have been swapped because the positional argument rule still applies
# So the default value has to come last

# To change the default value use this code

book_description('ashlee vance', book_type='fiction')