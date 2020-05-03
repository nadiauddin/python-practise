### 01/04/2020
### Nadia Uddin
### Override methods from parents class

# This method is in the ereader class
def describe_backlight(self):
    """Describes the backlight of our e-reader"""
    print("The backlight of this ereader allows you to read in the dark.")

# This method is in the kindle fire class which doesn't need a backlight because of its colour screen
# Overrides the method described in the parent method if using the same name for the method in the child's class
def describe_backlight(self):
    """The Kindle Fire doesn't have a backlight"""
    print("The colour screen lets you read in the dark.")
    