def merhaba(): #parametresiz fonksiyon
    print("Merhaba Python")

def first_program(language,ide): #parametreli fonksiyon
    print("Your using programming language :",language,"and ide :",ide)
    print("First Program: ")
    merhaba()

first_program("Python","Idle")

#fonksiyonlar da return deyimi

def delta_hesapla(a,b,c):
    return (b*b-4-a*c)

def kokbulma(a,b,c):
    delta=delta_hesapla(a,b,c)
    if(delta<0):
        print ("Reel kök yoktur")
        return 
    else:
        x1=(-b+delta*0.5)/(2*a)
        x2=(-b-delta*0.5)/(2*a)
        return (x1,x2)

a=input("a değerini girin:")
a=int(a)
b=input("b değerini girin:")
b=int(b)
c=input("c değerini girin:")
c=int(c)
print(kokbulma(a,b,c))
