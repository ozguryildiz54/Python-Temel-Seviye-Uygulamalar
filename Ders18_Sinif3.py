import random
class kumanda:
    def __init__(self,yenises=0,yenidurum=False,yenikanal=1,yeniliste=[1]):
        self.ses=yenises
        self.tvdurum=yenidurum
        self.kanal=yenikanal
        self.kanallistesi=yeniliste
    def goster(self):
        print("Ses :",self.ses)
        print("Tv durum :",self.tvdurum)
        print("Kanal Sayısı :",self.kanal)
        print("Kanal Listesi :",self.kanallistesi)
        print("------------------------------------------")
    def sesiartir(self,deger):
        self.ses+=deger
    def sesiazalt(self,deger):
        self.ses-=deger
    def kanalekle(self):
        for i in range(4,21):
            self.kanallistesi.append(i)
    def kanalsil(self,deger):
        self.kanallistesi.pop(deger)#deger degiskeni kacsa o indisde ki elaman silinir
    def tvkapat(self):
        self.tvdurum=False
    def tvac(self):
        self.tvdurum=True
    def rastgelekanal(self):
        rastgele=random.randint(4,29) #random sayı üretir
        kontrol=False
        son=int(len(self.kanallistesi))
        for i in range(0,son,1):
            if(rastgele==self.kanallistesi[i]):
                self.kanal=rastgele
                print("Yeni Kanal :",rastgele)
                kontrol=True
                break
            elif(i==(son-1)):
                if(kontrol==False):
                    print("Böyle bir kanal bulunumadı!")
nesne=kumanda()
nesne.goster()
nesne=kumanda(15,True,3,[1,2,3])
nesne.goster()
nesne.sesiartir(20)
nesne.goster()
nesne.sesiazalt(10)
nesne.goster()
nesne.kanalekle()
nesne.goster()
a=input("Kaçıncı kanalı silmek istersiniz? :")
a=int(a)
nesne.kanalsil(a)
nesne.goster()
nesne.tvkapat()
nesne.goster()
nesne.tvac()
nesne.goster()
nesne.rastgelekanal()
nesne.goster()
        





        
        
