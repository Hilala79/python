print("""
Mükemmel sayı 
"""
)
while True:
    sayı = int(input("lütfen bir sayı giriniz:"))
    bölentoplam =0
    for i in range(1,sayı):
        if sayı % i ==0:
            bölentoplam += i

    if bölentoplam == sayı:
        print("mükemmel sayı")
    else:
        print ("mükemmel satı değil")




