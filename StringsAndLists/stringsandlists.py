words = "It's Thanksgiving day. It's my birthday, too!"
print words.find('day')


words = "It's Thanksgiving day. It's my birthday, too!"
new_words = words.replace( 'day', 'month', 1)
print new_words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[7]
print [y[0], y[-1]]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z

a = z[:len(z)/2]
b = z[len(z)/2:]
print a
print b

b.insert(0,a)
print b