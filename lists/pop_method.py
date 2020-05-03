# 03/02/2020
# Author: Nadia Uddin
# Using the pop() method

# Use the pop() method when you want to remove an item from a list but still want to use that element
subscribers = ['nadia@example.com', 'john@example.com', 'shamyla@example.com']
print(subscribers)

# Not using an index removes the last item on the list
popped_subscriber = subscribers.pop()
print(subscribers)

# The subscriber that has been removed will be printed
print(popped_subscriber)

# Using the known index to print out a string with an element from the list
subscribers = ['nadia@example.com', 'john@example.com', 'shamyla@example.com']
first_subscriber = subscribers.pop(0)
print("your first subscriber was " + first_subscriber + ".")

# Resetting the list of subscribers
subscribers = ['nadia@example.com', 'john@example.com', 'shamyla@example.com']
print(subscribers)

# If you don't know the index but you know the email
subscribers.remove('john@example.com')
print(subscribers)

subscribers = ['nadia@example.com', 'john@example.com', 'shamyla@example.com']
subscribed_by_mistake = 'nadia@example.com'

subscribers.remove(subscribed_by_mistake)
print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")