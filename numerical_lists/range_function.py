# 04/02/2020
# Nadia Uddin
# range() function

# Using the range value to create  a list of numbers
for value in range(1,6):
    print(value)

# Converting numbers into a list
numbers = list(range(1,6))
print(numbers)

# 1st number is lower bound, 2nd is upper, 3rd is size step
odd_numbers = list(range(1,101, 2))
print(odd_numbers)

even_numbers = list(range(2,101, 2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = ['1','2','3','4','5']
print(max(digits))
print(min(digits))

digits = [1,2,3,4,5]
print(sum(digits))