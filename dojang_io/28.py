with open('file/word.txt', 'r') as file:
    words = file.readlines()
    
for index, word in enumerate(words) :
    words[index] = word.strip('\n')
    if words[index] == words[index][::-1]:
        print(words[index])