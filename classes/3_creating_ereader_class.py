### 02/04/2020
### Nadia Uddin
### Creating a new ereader class

class Ereader():
    """A class to represent an ereader"""
    def __init__(self, make, model, backlight, battery_life, screen_type):
        """Initialise the attributes to describe an ereader"""
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery_life = battery_life
        self.screen_type = screen_type

# Creating the title/name of our ereader that'd be shown at the top of Amazon
    def get_ereader_name(self):
        """Return a formatted descriptive name for our ereader"""
        long_name = self.make + " " + self.model + " - " + self.backlight + ", " + self.battery_life + ", " + self.screen_type
        return long_name.title()

my_new_ereader = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustible backlight', 'several months of battery life', '300 dpi')
print(my_new_ereader.get_ereader_name())