from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
label1 = Label(root,text='Hello World')
label1.pack()

def Tap():
    messagebox._show('YOU JUST CLICKED' , 'KAT GAYA TERA BC')

def Clear():
    e.delete(0,END)

def ShowOnLabel():
    labelText.set(e.get())

b = Button(root, text='click here' , command  = Tap) #refer to tap function above
b.pack()

Checkbutton(root, text="GO TO HELL").pack()

e = Entry(root, bg='red' , fg='yellow')
e.pack()
Button(root , text = 'CLEAR' , command = Clear).pack() #refer Clear function above

Button(root, text='SHOW' , command = ShowOnLabel).pack() #25 to 31 : showing entry text on a label. Refer ShoOnLabel function above

labelText = StringVar()
labelText.set('-------')

l = Label(root , textvariable = labelText)
l.pack()

ttk.Button(root , text='TTK').pack()

root.mainloop()
