### 02/04/2020
### Nadia Uddin
### Creating our first class

class Book():
    """"A class to create a book"""

# a function inside a class is called a method
# def __init___ is a method
    def __init__(self, name, price, publisher):
        """Initialise the name, price and publisher attributes"""

        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        """Simulate a hardback book"""
        print(self.name.title() + " is a hardback book.")

    def paperback(self):
        """Simulate a paperback book"""
        print(self.name.title() + " is a paperback book.")

    def ebook(self):
        """Simulate an ebook"""
        print(self.name.title() + " is an ebook.")

    def ebook_reader(self):
        """Simulate an ebook reader"""
        print("Library: " + self.name.title() + ", £" + str(self.price) + ", " + self.publisher.title() + ".")

# Creating an instance of our book class.
# my_book is an instance
# within the init parameters, the arguments are what's in the brackets
my_book = Book('elon musk', 14.99, 'virgin books')

# Accessing attributes
print("I am currently reading " + my_book.name.title() + ".")
print("This book cost " + "£" + str(my_book.price) + ".")

# Calling book type methods
my_book.paperback()
my_book.hardback()

# Calling our ebook_reader method
my_book.ebook_reader()

# Creating a second instance of the Book class
your_book = Book('the everything store', 9.99, 'virgin books')

your_book.hardback()