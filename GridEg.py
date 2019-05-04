from tkinter import *
from tkinter import ttk

root = Tk()

label1 = Label(root , text = 'X' , bg = 'white')
label1.grid(row = 0 , column = 0 , ipadx = 50 , ipady = 50) #padx and pady are of outer padding, ipadx and ipady are for inner padding
                                                            #inner padding simply increases the size of the grid block
label2 = Label(root , text = 'O' , bg = 'yellow')
label2.grid(row = 0 , column = 1 , sticky = N+S) #sticky helps in placing the label anywhere we want in the grid block itself
                                                #provided size of label is smaller then the grid block, label can be placed anywhere we want in
                                                #grid block : N,E,W,S or NE or SE or expand the label using N+S or E+W
label3 = Label(root , text = 'O' , bg = 'yellow')
label3.grid(row = 1 , column = 0 , sticky = N+W+E+S) #this expands the label in all the directions

label4 = Label(root , text = 'X' , bg = 'white')
label4.grid(row = 1 , column = 1 , ipadx = 50 , ipady = 50)



root.mainloop()
