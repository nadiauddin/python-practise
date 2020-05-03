### 01/04/2020
### Nadia Uddin
### Arbitrary arguments

# When we don't know how many arguments will need to be collected

# The asterisk allows Python to accept an arbitrary number of arguments
def create_passenger(*requests):
    """Print user requests in description"""
    print(requests)

create_passenger('window seat', 'seat near top of plane', 'leg room', 'pre-order breakfast')

def create_passenger(*requests):
    """Summarise passenger requests"""
    print("\n This passenger has requested: ")
    for request in requests:
        print("- " + request)


create_passenger('window seat', 'leg room', 'pre-order breakfast')