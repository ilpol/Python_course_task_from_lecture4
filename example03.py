#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Пример для первой лекции про TkInter
Закрытие окошка в постинтерактивном режиме
'''


from Tkinter import *
from random import randint


import random
TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)



colors = ["red", "white", "orange","peach puff","green2","LightPink2","salmon"]

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  


def random_color():
    Txt = Label(root, text="This is a label", bg=random.choice(colors))
    Txt.grid(row=1, column=1, columnspan=100, sticky=E+W+N+S)



def dump():
    #print("DUMP:",args)
    Butt2 = Button(root, text="New But",command = random_color)
    #Butt2.bind('<Button-2>', dump)
    Butt2.grid(row=1, column=0, sticky=E+W+S+N)
    Txt = Label(root, text="This is a label", bg=random.choice(colors))
    Txt.grid(row=1, column=1, columnspan=100, sticky=E+W+N+S)



#result = dump(root)
Butt = Button(root, text="Add", command = dump)
#Butt.bind('<Button-1>', dump(root))
Butt.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)


TKroot.mainloop()
print("Done")
#root.destroy()