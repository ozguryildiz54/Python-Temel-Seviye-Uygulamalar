class sinif: #sınıf tanımlaması bu sekilde yapılır
    mevcut=0

class kumanda:
                                     #Bu 1. kullanımıdır
    def __init__(self): #sınıfımızın yapılandırıcı metodudur
        self.ses=10 #self ifadesi java gibi dillerde ki this ifadesi gibidir
        self.kanal="Trt 1"

nesne=sinif()
print(nesne.mevcut)

nesne2=kumanda()
print("ses:",nesne2.ses)

class ev:
                                    #Bu da 2. kullanımdır
    def __init__(self,oda=4,fiyat=1600.56,esya=False):
        self.oda=oda
        self.fiyat=fiyat
        self.esya=esya

nesne3=ev(3,1400.5,True)
print("Oda sayısı :",nesne3.oda,"Fiyat :",nesne3.fiyat,"Esya :",nesne3.esya)

nesne4=ev()
print("Oda sayısı :",nesne4.oda,"Fiyat :",nesne4.fiyat,"Esya :",nesne4.esya)











        
