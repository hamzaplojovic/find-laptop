import tkinter
from tkinter import *

row = 1 
def create_row(text):
    global row
    link_button = Button(root, text=text, width=10, height=2)
    link_button.grid(row=row, column=0, padx=10, pady=5)

    link_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
    link_entry.grid(row=row, column=1, ipady=5)
    row += 1

    return link_entry

def calculate_index():
    pass
def db_values():
    pass


def add_command():

    
    values = {"link": link.get(),
              "price": price.get(),
              "cpu":   cpu.get(),
              "battery": battery.get(),
              "ram": ram.get(),
              "screen quality": sq.get(),
              "screen resolution": sr.get(),
              "state": state.get()}


  

    print(values)
#=======================================================

# Main window
root = tkinter.Tk()
root.title("Laptop Finder")
root.geometry("480x500")

#======================================================

#Button Add
add = Button(root, text="Add", width=5, command=add_command)
add.grid(row=9, column=2, padx=0, pady=10)

#=======================================================

link = create_row("Link")
price = create_row("Price")
cpu = create_row("CPU")
battery = create_row("Battery")
ram = create_row("RAM")
sq = create_row("Screen Q.")
sr = create_row("Screen R.")
state = create_row("State")

root.mainloop()