
# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for count in range(1, 1001): #creates a variable called Count to hold all of the numbers between 1 and 10001 
    print count #prints the variable


# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for count in range (5, 1000000): #creates a variable called count and assigns it a range of 5 to 10000000
    print count * 5 #prints the numbers in the range that are a  multiple of 5

#Sum List
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3] #Creates a variable called a, and assigns it the values inside
b = sum(a) #creates a variable called b and assigns it the sum of a
print b #prints variable b

#Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
c = [1, 2, 5, 10, 255, 3] #creates a variable called c and assigns it values
print sum(c)/len(c) #prints the sum of c divided by the length of c