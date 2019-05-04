from tkinter import *
from tkinter import messagebox

root = Tk()

def Save():
    messagebox._show('Message' , 'File saved successfully') #when save is clicked

def Close():
    exit()  #exit the window and stop the running process

menu = Menu(root)
root.config(menu = menu) #creating a menu bar

subMenu = Menu(menu , tearoff = 0) #adding options to the menu bar
                                #a dooted line is displayed on top of the dropdown menu, to remove it , tearoff = 0 is used
                                # it means remove the line at index 0 of the menu
menu.add_cascade(label = 'File' , menu = subMenu) #adds a dropdwon feature to the label at the menu bar
subMenu.add_command(label = 'Open') #options displayed on the dropdown menu when clicking the label
subMenu.add_command(label = 'Edit')
subMenu.add_command(label = 'Save' , command = Save)
subMenu.add_command(label = 'Save As')

subMenu.add_separator() #adds a separating grey line between 2 options(maybe of different category of operations)

subMenu.add_command(label = 'Close' , command = Close)
subMenu.add_command(label = 'Delete')

subMenu2 = Menu(menu , tearoff = 0)
menu.add_cascade(label = 'Edit' , menu = subMenu2)
subMenu2.add_command(label = 'Undo')
subMenu2.add_command(label = 'Copy')
subMenu2.add_command(label = 'Paste')

root.mainloop()