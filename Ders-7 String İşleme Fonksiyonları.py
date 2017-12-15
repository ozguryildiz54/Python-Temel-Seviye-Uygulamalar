a="metin"
print (len(a)) #metnin boyutunu hesaplar
print (a.count("a")) #metinde kaç tane a olugunu sayar
print (a.upper()) #metnin harflerini buyuk yapar
print (a.lower()) #metnin harflerini kucuk yapar
print (a.upper().lower()) #metnin harflerini once buyutup sonra kucultur
print (a.startswith("asd")) #eğer metin fonksiyonun parametresi ile baslarsa fonksiyon true degilse false deger dondurur
print (a.index("i")) #i harfinin metinde ki index'i bulunur.Ancak i harfi metinde yoksa program hata verir
print (a.find("i")) #i harfini metinde arar bulursa indis numarasını verir aksi halde yani bulamazsa -1 degeri dondurur
print (a.replace("n","l")) #metinde fonksiyon icinde ki ilk harfle ikinci harfi değiştirir
print (a.isdigit()) #metnin numerik olup olmadıgını kontrol eder numerikse true değilse false degeri dondurur
print (a.isalpha()) #metnin alfabetik yani sadece harflerden olup olmadığını kontrol eder sonuc olarak bool tipinde deger dondurur
print (a.isalnum()) #metinde numerik değerler olup olmadığını kontrol eder sonuc bool tipindedir
