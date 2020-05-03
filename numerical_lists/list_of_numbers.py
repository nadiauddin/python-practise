# 10/02/2020
# Nadia Uddin
# Creating a list of numbers

# Converting numbers into a list
numbers = list(range(1,6))
print(numbers)

# creating a list of the first ten square numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    print(squares)
    print(max(squares))

digits = [1,2,3,4,5]
print(min(digits))