for i in range(5):
    print(i)

print(range(5,10))

# measuring length of a, which will be 5, and taking its range

a = ['mary', 'had', 'a', 'little', 'lamb']
# for a in the range of 0 to 5, print the index
# and then pick out the index of i
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

# 1st number is lower bound, 2nd is upper bound, 3rd is step size
print(list(range(0, 20, 3)))