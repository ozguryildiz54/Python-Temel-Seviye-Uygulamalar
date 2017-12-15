secim="evet"
while(secim=="evet"):
    sayi1=float(input("Sayi gir:"))
    sayi2=float(input("Yeni bir sayı gir:"))
    islem=input("işlem seç:")
    if(islem=="+"):
        sonuc=sayi1+sayi2
        print("Sonuc: %s"%sonuc)
    elif(islem=="-"):
        sonuc=sayi1-sayi2
        print("Sonuc: %s"%sonuc)
    elif(islem=="*"):
        sonuc=sayi1*sayi2
        print("Sonuc: %s"%sonuc)
    elif(islem=="/"):
        sonuc=sayi1/sayi2
        print("Sonuc: %s"%sonuc)
    else:
        print("Hatalı giriş yaptınız")
    secim=input("Devam etmek için \"evet\" çıkmak için \"hayır\" yazın")
    
    

 
