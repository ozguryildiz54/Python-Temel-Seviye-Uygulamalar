global b
b="bu degisken evrensel bir degiskendir"
c="bu degisken de genel bir degiskendir"
def genel_degiskenler():
    a="bu genel bir degiskendir"
    print (a)

def evrensel_degiskenler(degisken):
    degisken="degiskenin icerigi bu cumle ile degismis oldu"
    print (degisken)
    global c
    c="ama artık bu degiskende hem global oldu hem de icerigi degisti"
    print(c)

genel_degiskenler()
#print a -> bu satır a degiskeni evrensel yani global olmadığından Idle söz dizimi hatası verir

print(c)
print (b)
evrensel_degiskenler(b)
print (b)
print(c)

#pass deyiminin 1. kullanımı boş method yazmak içindir. Yani metod tanımlanır ancak gövdesi olusturulmaz.
def bu_bos_metotdur():
    pass

#pass deyiminin 2. kullanımı ise metot icinde bir dongu tanımladığımızda contunie deyimi gibi hicbir sey yapmadan o satırı atlar ve dongunun basına gider
def pass_kullanimi():
    while(True):
        x=input("en kucuk asal sayı karakterini giriniz")
        x=int(x)
        if(x!=2):
            print("Yanlıs cevap tekrar dene!")
            pass
        elif(x==2):
            print("Dogru cevap metot burada sonlanıyor")
            return print(x)
       
pass_kullanimi()
