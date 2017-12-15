from __future__ import division #bölme işlemlerinde kesirli sonuc bulmaya yarar

vize=input("Vize notunuzu giriniz:")
final=input("Final notunuzu giriniz:")
vize=float(vize)
final=float(final)
basari_notu=vize*4/10+final*6/10
if(basari_notu>=90):
    print("Ders notunuz AA")
elif(basari_notu>=80):
    print("Ders notunuz BA")
elif(basari_notu>=70):
    print("Ders notunuz BB")
elif(basari_notu>=60):
    print("Ders notunuz CB")
elif(basari_notu>=50):
    print("Ders notunuz CC")
else:
    print("Dersten Kaldınız")
