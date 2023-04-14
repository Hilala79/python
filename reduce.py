from functools import reduce
def topla(x,y):
    return x+y
list = [1,2,3,4,5,6,7,8,9,10]

newlist =filter (lambda x:x%2==0, list)

print(reduce (topla, newlist))