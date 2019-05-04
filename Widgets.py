from tkinter import *

def PressForRed():
    labelText.set('KATEGA TERA')
    label.config(bg = 'red')

def PressForGreen():
    labelText.set('ABHI BHI KATEGA TERA')
    label.config(bg = 'green')

def PressForYellow():
    labelText.set('KATEGA HI KATEGA TERA')
    label.config(bg = 'yellow')

root = Tk()

labelText=StringVar()
labelText.set('HELLO WORLD')

label = Label(root, textvariable = labelText)
label.pack()  #on the next line because we want to use this label object for further use like changing bg color of label text etc etc

r =  Button(root, text="CLICK ME" , command = PressForRed)
r.pack()

g = Button(root, text="CLICK ME 2" , command = PressForGreen).pack()
b = Button(root, text="CLICK ME 3" , command = PressForYellow).pack() #parenthesis not required after function name call under command keyword

root.mainloop()