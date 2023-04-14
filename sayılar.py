print("""
büyük sayı bulma
 """)


s1=int(input("birinci sayı:"))
s2=int(input("ikinci sayı:"))
s3=int(input("üçüncü sayı:"))

if s1 >= s2:
    if s2 >= s3:
        print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s1,s2,s3))
    elif s1 >= s3:ş
        print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s1, s3, s2))
    else:
        print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s3, s1, s2))
elif s2 >= s3:
    if s1 >= s3:
        print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s2, s1, s3))
    else :
        print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s2, s3, s1))
else:
    print("birinci sayı:{} ikinci sayı:{} üçüncü sayı:{}".format(s3, s2, s1))
