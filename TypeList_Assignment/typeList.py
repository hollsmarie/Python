# If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. 
# At the end of your program print the string, 
# the number and an analysis of what the list contains. 
# If it contains only one type, print that type, 
# otherwise, print 'mixed'.


# if type(sI) == int and sI>101:
#     print("That's a big number!" )
# elif type(sI)==int and sI<101:
#     print("That's a small number!")

sum = 0
sent_str =""

my_input = ['magical unicorns',19,'hello',98.98,'world']
tempType = type(my_input[0])
for index in my_input:
    if type(index) == int:
        sum += index
    if type(index) == str:
        sent_str += str(index) + "-"
    if type(index) == float:
        float(index)
        sum += index  
print sum
print sent_str
if type(index)!= tempType:
    print("mixed")
elif type(index)==tempType:
    print("same type")

