def istriangle(list):
    a = list[0]
    b=list[1]
    c=list[2]
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7),(1, 2, 7)]

print(list(filter(lambda x: istriangle(x), liste)))


