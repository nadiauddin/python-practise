### 08/04/2020
### Nadia Uddin
### Read an entire file

# .strip takes away white space
with open('1_read_entire_file.txt') as file_object:
    contents = file_object.read()
    print(contents.title().strip())