#pyton kaynak kodlarının olusturulduğu her dosya moduldür
#eger eklenecek modul farklı klasorde ise cmd ile asagıdaki islemler yapılır
# cd dosya_yolu python yazılır ve python calıstırılır
#import modul_ismi
#modul_ismi.fonksiyon_ismi() diyerek kullanılabilir

#cmd ile ugrasılmak istenmiyorsa modul eklenecek dosya ile aynı konumda olmalıdır
import Ders16_Ozyinelemeli_Rekursif_Fonksiyonlar as a
# as ifadesi modul ismi uzun olan modullerinin
#adını as ifadesinin sagındaki ifade ile kullanabilmek icin kullanılır

a.faktoriyel(5) #bu tanımlama ile modulun tum metotlarına erisip kullanabilirim
print("Modülün İçeriği:",dir(a)) # modulun icinde ne kadar degisken ve metot tanımlaması varsa bu tanımlama ile görebilirim
#reload(a) modulde herhangi bir degisiklik yaptıysam bu metot ile tekrar yukluyorum

#------->bu iki tanımlama ile ekleme yapılırsa modulun ismini yazmaya gerek yok
#yani en altta ki tanımlama gibi
#from a import Ders16_Ozyinelemeli_Rekursif_Fonksiyonlar
#modulde ki tum tanımlamalar yuklenir
from Ders16_Ozyinelemeli_Rekursif_Fonksiyonlar import faktoriyel
#sadece faktoriyel metodu eklenir
print(faktoriyel(6))
#------->

import math
print(math.pi)
print("Matematik modülünde ki fonksiyonlar:",dir(math))
print(math.pow(33,45)) #üs alma fonskiyonu 33'ün 45'inci kuvveti (üssü)


