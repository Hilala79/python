str ="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
list1 = list(str)
print(list1)

sözlük = dict()

for  i in list1:
    if  i in sözlük:
        sözlük[i] +=1
    else:
        sözlük[i] =1
for i,j in sözlük.items():
    print("{} harfi {} kere".format( i,j))