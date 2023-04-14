print("""
Armstrong 
"""
)
while True:
    sayı = int(input("lütfen bir sayı giriniz:"))
    basamaksayısı =0
    index = 0
    found = 0
    while found == 0:

        if sayı / 10**index < 10:

            found = 1
            break
        else:
            index += 1
    print ("basamak sayısı =", index+1)
    toplam =0
    kalansayı=sayı
    print("1634//1000", 1634//1000)
    for i in range(0, index+1):

        toplam =toplam+(
                (kalansayı//(10**(index-i)))**(index+1))
        print("((10**(index-i)):", (10**(index-i)))
        basamak =(kalansayı//(10**(index-i)))
        print("basamak:", basamak)
        kalansayı = kalansayı - basamak * (10 ** (index-i))
        print("toplam ={} ".format(toplam))
    if toplam  == sayı:
        print ("toplam ={} armstrond sayı".format(toplam))
    else:
        print ("toplam ={} armstron sayı değil".format(toplam))




