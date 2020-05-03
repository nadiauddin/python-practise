### 01/04/2020
### Nadia Uddin
### Our module / importing an enitre module

# To use multiple times in a program or to share with other developers

def books_available(*books):
    """Show a list of books available to buy"""
    for book in books:
        books_in_stock = "The following title is available to buy " + book
        print(books_in_stock)

def book_description(author_name, book_type='non-fiction'):
    """Display book information"""

    print("\nThis is a " + book_type + " book.")
    print("The author of this book is " + author_name.title())