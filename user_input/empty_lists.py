### 17/02/2020
### Nadia Uddin
### Working with empty lists

# Empty shopping cart
shopping_cart = []

if shopping_cart:
    for item in shopping_cart:
        print("Adding " + item + " to your cart.")
    print("Your order is complete.")
else:
    print("You must select an item to before proceeding.")