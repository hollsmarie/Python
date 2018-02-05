
listone = [1,2,5,6,2]
listtwo = [1,2,5,6,2]

one = [1,2,5,6,5]
two = [1,2,5,6,5,3]

numberOne = [1,2,5,6,5,16]
numberTwo = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

list_one_1 = ['celery','carrots','bread','milk']
list_two_2 = ['celery','carrots','bread','cream']


def compare(list_one, list_two):
    if list_one == list_two:
        print ("The lists are the same")
    elif list_one != list_two:
        print("The lists are not the same")

compare(listone, listtwo)
compare(one, two)
compare(numberOne, numberTwo)
compare(list_one, list_two)
compare(list_one_1, list_two_2)