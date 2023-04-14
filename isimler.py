isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

#y =list(map(lambda x,y: x+" "+y, isimler,soyisimler))

#print (*y,sep="\n")



y = list(zip(isimler, soyisimler))

for (i,j) in y:
    print(i,j)

