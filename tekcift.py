def tekciftmi(sayı):
    if sayı%2 ==0:
        return sayı
    else:
        raise  ValueError("bu sayı tek bir sayıdır")

liste = [3,4,5,6,7,8]

for  i in liste:
    try:
        tekciftmi(i)
        print("\n",i)
    except ValueError:
        pass



