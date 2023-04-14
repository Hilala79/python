bjkliste=[]
gsliste=[]
fbliste=[]
with open ("futbolcular.txt","r",encoding ="utf-8") as file:
    liste = file.readlines()
    print(liste)
    for futbolcu in liste:
        içliste=futbolcu[:-1].split((","))
        if içliste[1]=="Beşiktaş":
            bjkliste.append((içliste[0]+"\n"))
        elif içliste[1]=="Galatasaray":
            gsliste.append((içliste[0]+"\n"))
        elif içliste[1]=="Fenerbahçe":
            fbliste.append((içliste[0]+"\n"))
    print(bjkliste)
    print(fbliste)
    print(gsliste)

    with open ("gs.txt","w",encoding ="utf-8") as file:
       file.writelines(gsliste)
    with open("fb.txt", "w", encoding="utf-8") as file:
       file.writelines(fbliste)
    with open("bjk.txt", "w", encoding="utf-8") as file:
        file.writelines(bjkliste)