words = "It's Thanksgiving day. It's my birthday, too!" # Creates a string called words
print words.find('day') #prints the index of the value words


words = "It's Thanksgiving day. It's my birthday, too!"
new_words = words.replace( 'day', 'month', 1) #creates a new string, and replaces the sub string day, with month, one time
print new_words #prints the new string

x = [2,54,-2,7,12,98] #creates a string called x
print min(x) #prints the minimum value in x
print max(x) #prints the maximum value in x

y = ["hello",2,54,-2,7,12,98,"world"] #creates a string called y
print y[0] #prints the 0 index of the y string
print y[7] #prints the last index of the y strijng
print [y[0], y[-1]] #prints the y string with only the first and last values

z = [19,2,54,-2,7,12,98,32,10,-3,6] #creates a string called z
z.sort() # sorts z from smallest to largest value
print z #prints the updated string

a = z[:len(z)/2] #cuts the string in half from beginning to middle
b = z[len(z)/2:] #cuts the string in half from middle to end
print a #prints the first half of the string
print b #prints the last half of the string

b.insert(0,a) #inserts the first half of the string in the 0 index of the second half of the string
print b #prints the updated string