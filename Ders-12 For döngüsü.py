liste=[1,2,3,4,5]
for i in liste:
    print (i)
print(range(3,15,3))#range fonksiyonu 3 den baslayarak 15 e kadar 3'er 3'er gider
range(0,10)#0 dan 10 a kadar ardışık olarak artar

for i in range(0,10):
    if(i%2==0):
        print (i)
string="gollum"
for i in string:
    print (i)
demet=(5,3,7,1,7,3,5)
for i in demet:
    print (i*"*")

a=0
while(a<len(demet)):
    print (demet[a])
    a=a+1

