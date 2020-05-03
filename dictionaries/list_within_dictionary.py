### 18/02/2020
### Nadia Uddin
### Using a list within a dictionary

car = {
    'type':'standard four door saloon',
    'extras':['alloy wheels', 'climate control', 'heated seats'],
}

# Print order summary ummary
print("The car you have ordered is a " + car['type'] + " with the following extras: ")

for extra in car['extras']:
    print("\t" + extra)