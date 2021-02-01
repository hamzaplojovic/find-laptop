import tkinter
from tkinter import *

root = tkinter.Tk()


mydict = [
    {
        'link': 'kp.com/3',
        'price': 250,
        'cpu': 'i7-7700hq',
        'efficiency': 53,
    },
    {
        'link': 'kp.com/2',
        'price': 180,
        'cpu': 'i7-2530hq',
        'efficiency': 55,
    }
]

variable = mydict[0]['link']
label_1 = tkinter.Label(root, text=variable)
label_1.pack()

root.mainloop()