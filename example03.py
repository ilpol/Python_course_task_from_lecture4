#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''


from Tkinter import *
from random import randint
TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)



colors = ["red", "green", "blue"]

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  


def random_color():
    Txt = Label(root, text="This is a label", bg=_from_rgb((randint(0, 255), randint(0, 255), randint(0, 255))))
    Txt.place( x = 80,y = 55)



def dump():
    #print("DUMP:",args)
    Butt2 = Button(root, text="New But",command = random_color)
    #Butt2.bind('<Button-2>', dump)
    Butt2.place( x = 0,y = 50)
    Txt = Label(root, text="This is a label", bg=_from_rgb((randint(0, 255), randint(0, 255), randint(0, 255))))
    Txt.place( x = 80,y = 55)



#result = dump(root)
Butt = Button(root, text="Add", command = dump)
#Butt.bind('<Button-1>', dump(root))
Butt.place( x = 0,y = 0)
Exit = Button(root, text="Exit", command=root.quit)
Exit.place( x = 50,y = 0)


TKroot.mainloop()
print("Done")
#root.destroy()
