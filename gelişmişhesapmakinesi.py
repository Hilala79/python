import calculator

print("1. işlem: sinüs")
print("2. işlem: logaritma")
print("3. işlem: karesini alma")
print("4. çıkış")
while True:
    işlem = int(input("işlem seçimi:"))
    sayı = int(input("sayı giriniz:"))

    if işlem ==1:
        print ("sayı",sayı, " sinüs değeri:",calculator.sinüs(sayı))

    elif işlem == 2:
        print("sayı", sayı, " logaritma değeri:", calculator.logaritma(sayı))

    elif işlem == 3:
        print("sayı", sayı, " karesi:", calculator.karesi(sayı))

    else:
        break