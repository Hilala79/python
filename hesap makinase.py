print("""
Hesap makinası
1-Toplama işlemi
2-Toplama işlemi
3-Toplama işlemi
4-Toplama işlemi


""")
s1=int(input("birinci sayı:"))
s2=int(input("ikinci sayı:"))
i1=input("işlem:")


if i1=="1":
    print("{} ile {} nın toplamı={}".format(s1,s2,s1+s2) )
elif i1=="2":
    print("{} ile {} nın farkı={}".format(s1, s2, s1 - s2))
elif i1=="3":
    print("{} ile {} nın çarpımı={}".format(s1, s2, s1 * s2))
elif i1=="4":
    print("{} ile {} nın bölümü={}".format(s1, s2, s1 / s2))
else:
    print("geçerli işlem seçiniz...")