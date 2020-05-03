### 01/04/2020
### Nadia Uddin
### Inheritance - To avoid starting from scratch when using classes

# Original class is called the parent class
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
        return long_name.title()

    def read_library_count(self):
        """Show the amount of ebooks in our kindle library"""
        print("You have " + str(self.library_count) + " books in your Kindle library.")

    def update_library_count(self, ebook_count):
        """Set the library count"""
        self.library_count = ebook_count

    def increment_library_count(self, purchased_ebooks):
        """Adding new ebooks to our library count"""
        self.library_count += purchased_ebooks

# New class is called child class - has all the same attributes as parent but can add its own

class KindleFire(Ereader):
    """Represents aspects of an ereader specific to a Kindle Fire"""

    def __init__(self, make, model, backlight, battery_life, screen_type, screen_resolution='1280 * 800'):
        """Initialise attributes of the parent class.
            Then initialise attributes specific to a Kindle Fire"""
    self.screen_resolution = screen_resolution
     # super function helps python make connection between parent and child class.
    super().__init__(make, model, backlight, battery_life, screen_type)

    def describe_screen(self):
        """Print out some marketing info about the Kindle Fire"""
    print("\nFire HD 8 features a widescreen " + self.screen_resolution + " HD screen.")

my_kindle_fire = KindleFire('amazon', 'kindle fire', 'backlight', '12 hour battery life', 'touch screen')
print(my_kindle_fire.get_ereader_name())

my_kindle_fire.describe_screen()