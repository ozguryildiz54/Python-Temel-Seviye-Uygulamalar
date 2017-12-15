"""
import tkinter
print(dir(tkinter))
"""
from tkinter import *
pencere=Tk() #Form olusturma sınıfı
etiket=Label(pencere,text="Merhaba Dünya") #Label olusturuldu
etiket.pack()
pencere.mainloop()
