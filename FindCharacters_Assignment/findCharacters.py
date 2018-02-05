# input

word_list = ['hello','world','my','name','is','Holly']
char = 'o'
string = word_list[0]
new_list = []
for string in word_list:
    for char in string:
        if char == 'o':
            new_list.append(string)
print new_list