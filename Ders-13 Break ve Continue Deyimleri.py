user="admin"
password="sanane"
secim="e"
hata="error"
while(secim=="e"):
    input1=input("Kullanıcı Adı:")
    if(user==input1):
        input2=input("Şifre:")
        if(password==input2):
            print("Giriş Başarılı")
            numaralar=[2,4,6]
            for i in range(0,15):
                if (i in numaralar):
                    continue
                print(i)
        else:
            print("Şifre Yanlış")
    else:
        print("Kullanıcı Adı Yanlış")
    secim=input("Devam etmek istermisiniz?  :")#donguyu kırmak icin \"h\" devam etmek icin \"e\" ye basınız
    while(secim!="h" or secim!="e"):
           secim=input("Hatalı giriş yaptınız tekrar deneyiniz!  :")
           if(secim=="e" or secim=="h"):
               break
    if(secim=="h"):
        print("Çıkış yapıldı")
        break
    
        
