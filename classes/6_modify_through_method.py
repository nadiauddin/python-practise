### 02/04/2020
### Nadia Uddin
### Modifying an attribute by creating a new method to do so

class Ereader():
    """A class to represent an ereader"""
    def __init__(self, make, model, backlight, battery_life, screen_type):
        """Initialise the attributes to describe an ereader"""
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery_life = battery_life
        self.screen_type = screen_type
     # default value here is 0
        self.library_count = 0

    def get_ereader_name(self):
        """Return a formatted descriptive name for our ereader"""
        long_name = self.make + " " + self.model + " - " + self.backlight + ", " + self.battery_life + ", " + self.screen_type
        return long_name

    def read_library_count(self):
        """Show the amount of ebooks in our kindle library"""
        print("You have " + str(self.library_count) + " books in your Kindle library.")

    def update_library_count(self, ebook_count):
        """Set the library count"""
        self.library_count = ebook_count

my_new_ereader = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustible backlight', 'several months of battery life', '300 dpi')
print(my_new_ereader.get_ereader_name().title())

# MODIFICATION IS HERE
my_new_ereader.update_library_count(20)
my_new_ereader.read_library_count()