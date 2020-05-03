### 17/02/2020
### Nadia Uddin
### Interest rate checker using if-elif-else

# Get user balance
balance = input("What is your current bank balance? ")

if int(balance) <= 0:
    print(input("Would you like to make a deposit?"))
elif int(balance) <=50:
    print("You do not qualify for interest.")
elif int(balance) < 100:
    print("Your interest rate is 1%.")
else: print("Your interest rate is 2%.")

