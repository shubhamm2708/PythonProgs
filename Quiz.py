from tkinter import *
from tkinter import messagebox

root = Tk()

def showVal():
    print(RBVal.get())
    #messagebox._show('Message','Nice')

RBVal = IntVar() #will return an integer. If value is a string change IntVar() to StringVar().

Label(root , text = 'SELECT YOUR FAV COLOR....').pack()
Radiobutton(root , text = 'Red' , value = 1 , variable = RBVal).pack() #value can be a string as well
Radiobutton(root , text = 'Blue' , value = 2 , variable = RBVal).pack()
Radiobutton(root , text = 'Yellow' , value = 3 , variable = RBVal).pack()
Radiobutton(root , text = 'Green' , value = 4 , variable = RBVal).pack()

Button(root , text = 'Show Value' , command = showVal).pack()
root.mainloop()