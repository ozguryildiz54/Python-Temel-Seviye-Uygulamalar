demet=("ozgur","yıldız",1995) #tuple (demet) tanımlaması
print(type(demet)) #demetin tipini gösterir
yeniDemet="adapazarı","sakarya",54 #buda bir demettir
print(type(yeniDemet))
a=() #bu da bir demettir ancak bos demet
print(type(a))
b=("sivas")  #bu demet değildir. bu str tipinde bir degişkene deger yuklemesidir
print(type(b))
c=("cumhuriyet universitesi",) #bu tek elemanlı bir demettir
print(type(c))
d=(1,2,3)
#d[0]=5 seklinde bir tanımlama yapılamaz
#bu tanımlama listeler de mumkundur
isim="ozge"
isim=isim[:3]+"ür"
print (isim) #ekran çıktısı olarak "özgür" yazar
meyve=("badem","kayısı","seftali")
badem,kayisi,seftali=meyve
print(badem,seftali,kayisi)
sayi1=54
sayi2=58
print("sayi1: %s ve sayi2: %s"%(sayi1,sayi2))
sayi1,sayi2=sayi2,sayi1 #degerler karsılıklı olarak degisir
print("sayi1: %s ve sayi2: %s"%(sayi1,sayi2))
print(len(demet)) #demetin kaç elamana sahip oldugunu hesaplar

