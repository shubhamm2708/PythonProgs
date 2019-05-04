from tkinter import *

root = Tk()

def ShowTable() :
    t=e.get()
    two = int(t) * 2
    three = int(t) * 3
    four = int(t) * 4
    five = int(t) * 5
    six = int(t) * 6
    seven = int(t) * 7
    eight = int(t) * 8
    nine = int(t) * 9
    ten = int(t) * 10

    lt.set(t + ' x 1 = ' + t)
    lt2.set(t + ' x 2 = ' + str(two))
    lt3.set(t + ' x 3 = ' + str(three))
    lt4.set(t + ' x 4 = ' + str(four))
    lt5.set(t + ' x 5 = ' + str(five))
    lt6.set(t + ' x 6 = ' + str(six))
    lt7.set(t + ' x 7 = ' + str(seven))
    lt8.set(t + ' x 8 = ' + str(eight))
    lt9.set(t + ' x 9 = ' + str(nine))
    lt10.set(t + ' x 10 = ' + str(ten))

e = Entry(root)
e.pack()

Button(root, text = 'Click' , command = ShowTable).pack()

lt = StringVar()
lt.set('------')
Label(root , textvariable = lt, bg='green').pack()

lt2 = StringVar()
lt2.set('------')
Label(root , textvariable = lt2, bg='yellow').pack()

lt3 = StringVar()
lt3.set('------')
Label(root , textvariable = lt3, bg='blue').pack()

lt4 = StringVar()
lt4.set('------')
Label(root , textvariable = lt4, bg='pink').pack()

lt5 = StringVar()
lt5.set('------')
Label(root , textvariable = lt5, bg='brown').pack()

lt6 = StringVar()
lt6.set('------')
Label(root , textvariable = lt6, bg='cyan').pack()

lt7 = StringVar()
lt7.set('------')
Label(root , textvariable = lt7, bg='magenta').pack()

lt8 = StringVar()
lt8.set('------')
Label(root , textvariable = lt8, bg='purple').pack()

lt9 = StringVar()
lt9.set('------')
Label(root , textvariable = lt9, bg='grey').pack()

lt10 = StringVar()
lt10.set('------')
Label(root , textvariable = lt10, bg='red').pack()

root.mainloop()