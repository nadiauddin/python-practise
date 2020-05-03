### 18/02/2020
### Nadia Uddin
### Using while loops to quit a program

current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# Using a while loop to quit a program

prompt = "\nTo end this program enter 'q'."
prompt += "\nPlease enter your name: "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)