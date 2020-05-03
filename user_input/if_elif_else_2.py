### 17/02/2020
### Nadia Uddin
### If one test has passed, Python skips the rest
### Sometimes you need to check if all the conditions are met

# Create a list of booking details
booking_details = ['nadia', 'middle row', 'screen two']
if 'nadia' in booking_details:
    print("Welcome to Odeon cinema.")
if 'middle row' in booking_details:
    print("Your seat number is A23 in the middle row.")
if 'screen two' in booking_details:
    print("Your movie will be shown in screen two.")