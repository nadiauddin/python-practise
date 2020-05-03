### 01/04/2020
### Nadia Uddin
### Using positional and arbitrary arguments together

# Arbitrary args must come after positional

def assign_seat(seat, *requests):
    """Assign a seat and requests to passenger"""
    print("\nAssign seat number " + str(seat) + " the following passenger requests:")
    for request in requests:
        print("- " + request)

assign_seat(36, 'window seat')