### 17/02/2020
### Nadia Uddin
### Working with multiple lists

in_stock = ['blue pens', 'black pens', 'paper']

shopping_cart = ['blue pens', 'paper', 'orange post-its']

for item in shopping_cart:
    if item in in_stock:
        print("Adding " + item + " to your cart.")
    else: print("Sorry, " + item + " is out of stock")
print("Your order is complete.")