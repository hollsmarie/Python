
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



def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

def layered_multiples(arr):
    new_array = []
    i=0
    while i < 3:
        new_array.append(arr[i]* "1")
        i+=1
    print new_array

x = layered_multiples(multiply([2,4,5],3))
