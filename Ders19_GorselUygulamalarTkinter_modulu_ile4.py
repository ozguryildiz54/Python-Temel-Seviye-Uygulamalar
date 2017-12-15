from tkinter import *
pencere=Tk()
def yaz():
    print("Butona basıldı!")
def yazdir(event):
    print("Butona basıldı!")
cerceve=Frame(pencere)
cerceve2=Frame(pencere)
cerceve.pack()
cerceve2.pack()

button=Button(cerceve,text="Yaz",fg="brown",command=yaz)
button2=Button(cerceve2,text="Yazdır",fg="brown")
button.pack()
button2.bind("<Button-1>",yazdir)
button2.pack()
#command=yaz ifadesi ile yaz metodu çalıştırılır
#yaz yerine çalıştırılmak istenen her hangi bir
#metot yazılabilir
