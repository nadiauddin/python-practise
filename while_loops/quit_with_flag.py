### 19/02/2020
### Nadia Uddin
### Using a flag to quit a program

#e.g. if your game player dies in a game

prompt = "Enter 'q' to end this program. "
prompt += "\nWhat is your name? "

# Set flag to True
active = True
while active:
    message = input(prompt)

    if message == 'q':
        active = False
    else: print(message)