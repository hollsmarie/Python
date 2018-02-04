# Shows your strings and variables when you run "python _name of file_" from terminal
print "Hello World!"
x = "Hello Python"
print x
y = 42
print y



#How to print strings using variables
print  "this is a simple string"
name = "Zen"
print "My name is", name
print "My name is " + name

#Example of Interpolation using {} and the .format()
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name,last_name)

#Another example of Interpolation
hw = "hello %s" % 'world'
print hw

#Built-In String Methods
x = "Hello World"
print x.upper()
# When you run "puython 'name of file'" in terminal
#this prints HELLO WORLD, print x.upper shows in caps

# string.count(substring): returns number of occurrences of substring in string.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

#Examples of lists, which are like arrays in JS
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

#Accessing values in Python
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

#Manipulating lists:
<list>.append(<new_element>)

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

#len(sequence): Returns the number of items in a sequence.

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3