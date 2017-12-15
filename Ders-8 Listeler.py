list=[1,2,"uc",True] #liste tanımlaması
print (list)

print (list[2])
print (list[-1])
print (list[1:])
print (list[1:2])
print (list[3])
print (list[::2])
print (list[::-1])

liste=[1,2,3,"adapazari"]
print(len(liste)) #listenin boyutunu hesaplar
a=[1,2,3,4,2,[3,4]]
print (len(a))
liste.append("sakarya") #listenin sonuna yeni bir elaman ekler
liste.extend([4,5,6,["sivas"]]) #listenin sonuna istenildiği gibi elaman eklenebilir.
a.count(3) #3 sayısının listede kaç tane olduğunu hesaplar
a.index(2) #2 sayısının listede ki konumu öğrenir
a.remove(1) #en bastan baslayarak ilk karsılastıgı 2 rakamını siler
#a.remove() #listenin en basında ki elamanı listeden siler
a.pop() #listenin en sonunda ki elamanı siler
liste.pop(2) #listenin 2. indisinde ki elamanı siler
a.insert(0,"ozgur") #listenin 0. indisine "ozgur" elamanını ekler
b=[3,67,33,76,123]
c=["q","e","r"]
c.sort() #listeyi alfabetik olarak sıralar
b.sort() #listeyi kucukten buyuge sıralar
b.reverse() #listenin elamanlarının sırasını simetrik olarak yer değiştirir.
"ozgur" in a #"ozgur" a listesinde mi diye kontrol ediyoruz.Cevabı boolean tipindedir.
"yıldız" not in a # "yıldız" a listesin de yok değil mi diye soruyoruz.
del a[0] # listenin 0. indisinde ki elamanı siler
kelime="ozgur,yıldız,sakarya"
liste=kelime.split(',')
print (liste)
