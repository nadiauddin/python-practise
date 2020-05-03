### 18/02/2020
### Nadia Uddin
### Using a dictionary in a list

# When you have multiple books which are dictionaries
# You can put these dictionaries in lists

book_0 = {
    'name': 'elon musk',
    'author': 'ashlee vance',
    'price': 14.99,
    'publisher': 'virgin books'
}

book_1 = {
    'name': 'team of rivals',
    'author': 'doris kearns',
    'price': 11.99,
    'publisher': 'not avail'
}

book_2 = {
    'name': 'kafka on the shore',
    'author': 'haruki murakami',
    'price': 7.91,
    'publisher': 'vintage'
}

books = [book_0, book_1, book_2]

for book in books:
    print(book)

# Using a dictionary within a list

stock_items = []

for blue_pen in range(0,50):
    new_blue_pen = {'colour':'blue', 'type':'ballpoint', 'price':'1.99'}
    stock_items.append(new_blue_pen)
# Make 50 blue pens - will print the info of 50 blue pens
print(stock_items)
# use a for loop and if statement to change the pen's price
# Changing the price of the first 5 pens

for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '1.99':
        blue_pen['price'] = '0.99'

for blue_pen in stock_items[0:5]:
    print(blue_pen)