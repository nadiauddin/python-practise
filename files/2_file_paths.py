### 08/04/2020
### Nadia Uddin
### File paths

with open('text_files/1_read_entire_file_copy.txt') as file_object:
    contents = file_object.read()
    print(contents.title().strip())

file_path = 'Users/nadiauddin/PycharmProjects/skillshare/files/text_files/1_read_entire_file_copy.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.title().strip())