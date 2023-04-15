from functools import reduce
def birlestir(x,y):
     return x[0]+y[0]
class Şiir:
    def __init__(self):
        with open ("şiir.txt","r",encoding ="utf-8") as file:
            siir_içerik = file.read()
            self.satırlar = siir_içerik.split("\n")
            print (self.satırlar)
    def ilkharf(self):
        list_new = [x[0] for x in self.satırlar]
        print("".join(list_new))

siir=Şiir()
siir.ilkharf()