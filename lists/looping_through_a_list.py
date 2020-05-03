# 04/02/2020
# Nadia Uddin
# Looping through a list
# used to carry out the same operation to all elements in a list

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
print(months[0])

# using a for loop to print a list
# for first element in list
# the for loop will repeat the process until the end - a process of elimination
for month in months:
    print(month.title() + "\n")
    print("The next month is ")

print("Goodbye!")
# anything more written in the indent even on a new line would be considered in the loop
# so each indented line is executed for each element in the list