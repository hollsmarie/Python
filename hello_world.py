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

def add(a,b): #we've named the function 'add' and given it to parameters(or inputs to the function)
    x = a + b
    return x #we return something
print add(3,5) #prints the answer

def say_hi(name): #function that has one parameter/input
    print "Hi, "+ name
say_hi('holly') #invokes the function and passes in one argument.

#name is the parameter
#holly is the argument
#we define parameters
#we pass in arguments

def say_hi():
  return "Hi"
greeting = say_hi() #the returned value from say_hi function gets assigned to the 'greeting' variable
print greeting #this will output 'Hi'

sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

def add(a, b):
  x = a + b
  return x
print sum1
print sum2
print sum3

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b



dog = ("Canis Familiaris", "dog", "carnivore", 12)
print dog[2]
for data in dog:
    print data
dog = dog + ("domestic",)
print dog
dog = dog[:3] + ("mans best friend",) + dog[4:]
print dog

def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
    print c,a

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
    for value in data:
        print "Question #", value["id"], ":", value["content"]
        print "----"


data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
print data.keys()
print data.values()


dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities = zip(countries, dishes)
print country_specialities

country_specialities_dict = dict(country_specialities) 
print country_specialities_dict