import tkinter
from tkinter import *
import webbrowser

root = tkinter.Tk()
root.title("Find Laptop")
root.geometry('1280x800')

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

row = 0

def create_row(link, price, cpu, efficiency):
    global row
    l1 = Label(root, text = f"CPU: {cpu} - ", font=('Calibri', 24)) 
    l2 = Label(root, text = f"Efficiency: {efficiency} - ", font=('Calibri', 24)) 
    l3 = Label(root, text = f"Price: {price} - ", font=('Calibri', 24)) 
    l4 = Label(root, text = f'{link} ', fg="blue",  cursor="hand2")
    
    # grid method to arrange labels in respective 
    # rows and columns as specified 
    l1.grid(row = row, column = 0, sticky = W, pady = 2) 
    l2.grid(row = row, column = 1, sticky = W, pady = 2) 
    l3.grid(row = row, column = 2, sticky = W, pady = 2) 
    l4.grid(row = row, column = 3, sticky = W, pady = 2)
    l4.bind("<Button-1>", callback) 
    row += 1


mydict = [
    {
        'link': 'https://www.kupujemprodajem.com/odmor-u-srbiji/tara/vila-fila/oglas/96020182',
        'price': 250,
        'cpu': 'i7-7700hq',
        'efficiency': 53,
    },
    {
        'link': 'https://www.kupujemprodajem.com/domaca-hrana/torte-i-kolaci/mafin/oglas/109751865',
        'price': 180,
        'cpu': 'i7-2530hq',
        'efficiency': 55,
    }
]


for x in mydict:
    # getting items from list
    link = x['link']
    price = x['price']
    cpu = x['cpu']
    efficiency = x['efficiency']

    # create labels on GUI tkinter
    create_row(link, price, cpu, efficiency)

root.mainloop()