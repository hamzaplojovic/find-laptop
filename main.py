import tkinter
from tkinter import *


def add_command():
    values = {"price": price_entry.get(),
              "cpu":   cpu_entry.get(),
              "battery": battery_entry.get(),
              "ram": ram_entry.get(),
              "screen quality": sq_entry.get(),
              "screen resolution": sr_entry.get(),
              "state": state_entry.get()}
    print(values)


# Main window
root = tkinter.Tk()
root.title("Laptop Finder")
root.geometry("800x800")
#======================================================
# Link
link_button = Button(root, text="Link", width=10, height=2)
link_button.grid(row=1, column=0, padx=10, pady=5)

link_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
link_entry.grid(row=1, column=1, ipady=5)
#=======================================================
# Price
price_button = Button(root, text="Price", width=10, height=2)
price_button.grid(row=2, column=0, padx=10, pady=5)

price_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
price_entry.grid(row=2, column=1, padx=0, pady=5, ipady=5)
#=======================================================
# CPU
cpu_button = Button(root, text="CPU", width=10, height=2)
cpu_button.grid(row=3, column=0, padx=10, pady=5)

cpu_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
cpu_entry.grid(row=3, column=1, ipady=5)
#=======================================================
# Battery
battery_button = Button(root, text="Battery", width=10, height=2)
battery_button.grid(row=4, column=0, padx=10, pady=5)

battery_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
battery_entry.grid(row=4, column=1, ipady=5)
#=======================================================
# RAM
ram_button = Button(root, text="RAM", width=10, height=2)
ram_button.grid(row=5, column=0, padx=10, pady=5)

ram_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
ram_entry.grid(row=5, column=1, ipady=5)
#=======================================================
# Screen Quality
sq_button = Button(root, text="Screen Q.", width=10, height=2)
sq_button.grid(row=6, column=0, padx=10, pady=5)

sq_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
sq_entry.grid(row=6, column=1, ipady=5)
#=======================================================
# Screen Resolution
sr_button = Button(root, text="Screen R.", width=10, height=2)
sr_button.grid(row=7, column=0, padx=10, pady=5)

sr_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
sr_entry.grid(row=7, column=1, ipady=5)
#=======================================================
# State
state_button = Button(root, text="State", width=10, height=2)
state_button.grid(row=8, column=0, padx=10, pady=5)

state_entry = Entry(root, width=40, bg="#EEEEEE", bd=3, font=("Calibri", 12))
state_entry.grid(row=8, column=1, ipady=5)
#=======================================================
#Button Add
add = Button(root, text="Add", width=5, command=add_command)
add.grid(row=9, column=2, padx=0, pady=10)
#=======================================================


root.mainloop()