from tkinter import *
pencere=Tk()
username=Label(pencere,text="Username :")
password=Label(pencere,text="Password :")
username.grid(row=0,column=0,sticky=E)
#sticky=E bu tanımlama yazının sağa yaslanmasını sağlıyor
#E east ( doğu anlamındadır )
password.grid(row=1,column=0,sticky=E)

entry=Entry(pencere)
entry.grid(row=0,column=1)
entry2=Entry(pencere)
entry2.grid(row=1,column=1)
#row ve column degerlerine göre ekranda farklı
#alanlarda konum alabilirler

tik=Checkbutton(pencere,text="Beni Hatırla")
tik.grid(columnspan=2)

pencere.mainloop()
