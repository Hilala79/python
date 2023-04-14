def mukemmessayımı(sayı):
    bolentoplam = 1
    for i in range(2 , sayı):
        if sayı % i == 0 :
            bolentoplam += i
    if sayı == bolentoplam:
        return True
    else:
        return False

while True:
    sayı = input("sayı:")
    if sayı =="q":
        print ("program sonlandırılıyor")
        break
    else:
        sonuc = mukemmessayımı(int(sayı))
        if sonuc==True:
            print ("sayı:", sayı,"mükemmel sayıdır")
        else:
            print("sayı:", sayı, "mükemmel sayıd değildir")