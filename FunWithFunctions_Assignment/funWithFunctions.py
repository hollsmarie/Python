def oddOrEven():
    for index in range(1,2001):
        if index%2 != 0:
            print "Number is", index,". This is an odd number."
        elif index%2 == 0:
            print "Number is", index,". This is an even number."
oddOrEven()

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

def layered_multiples(arr):
    for x in range(len(arr)):
        arr[x]*= arr
    return arr
x = layered_multiples(multiply([2,4,5],3))
print x
