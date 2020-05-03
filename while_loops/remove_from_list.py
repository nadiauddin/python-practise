### 19/02/2020
### Nadia Uddin
### Using while loop to remove all instances of a value from a list

books = ['big data', 'checklists', 'the firm', 'tesla', 'the firm', 'the firm']

while 'the firm' in books:
    books.remove('the firm')

print(books)