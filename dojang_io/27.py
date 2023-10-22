
with open("file/27.txt",'r') as file:
    contents = file.read()
    
list_contents = contents.split(' ')
for index, content in enumerate(list_contents) :
    list_contents[index] = content.strip(',.')
    if 'c' in list_contents[index] :
        print(list_contents[index])