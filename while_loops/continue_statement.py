### 19/02/2020
### Nadia Uddin
### Using Continue in a loop

# If current number divided by 2 has no remainder, continue the loop until you get to 9
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

print(current_number)