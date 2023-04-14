print("""
Beden kitle indexi hesaplama
""")

b1 = float(input("Boyunuzu giriniz:"))
k1 = int(input("kilonuzu giriniz:"))

bk1 = k1/(b1**2)
print("beden kitle indexi=",bk1)
if bk1<18.5:
    print("zayıf")
elif bk1<25:
    print("normal")
elif bk1 < 30:
    print("fazla kilolu")
else :
    print("obez")