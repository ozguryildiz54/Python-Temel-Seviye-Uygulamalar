from tkinter import *
pencere=Tk()

cerceve=Frame(pencere)
cerceve.pack()
cerceve2=Frame(pencere)
cerceve2.pack(side=BOTTOM)

button=Button(cerceve,text="Buton 1",fg="brown")
button.pack(side=LEFT)
button2=Button(cerceve,text="Button 2",fg="green")
button2.pack(side=RIGHT)

pencere.mainloop()
