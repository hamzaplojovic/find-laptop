import tkinter
from tkinter import *
from pymongo import MongoClient
import csv

client = MongoClient('localhost', 27017)

db = client['mydb']

collection = db['Laptops']

def get_data():
    data = {}
    f = open('cpu.csv')
    reader = csv.reader(f)
    for x in reader:
        data[x[3].lower()] = x[5]
    return data

    f.close()


def move_command():
    import ispis

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

    
    values = {
                "link": link.get(),
                "price": price.get(),
                "cpu":   cpu.get(),
                "efficiency" : efficiency.get()
              }


#   "battery": battery.get(),
#               "ram": ram.get(),
#               "screen quality": sq.get(),
#               "screen resolution": sr.get(),
#               "state": state.get()

    collection.insert_one(values)

#=======================================================

# Main window
root = tkinter.Tk()
root.title("Laptop Finder")
root.geometry("480x500")




#======================================================

#Button Add
add = Button(root, text="Add", width=5, command=add_command)    #add_command
add.grid(row=9, column=0, padx=0, pady=20)

#=======================================================

move_button = Button(root, text="Reader", width=5, command=move_command)
move_button.grid(row=9, column=2, padx=0, pady=20)

#=======================================================

link = create_row("Link")
efficiency = create_row("Efficiency")
price = create_row("Price")
cpu = create_row("CPU")

def button_click():
    efficiency.delete(0, END)
    efficiency.insert(0, data.get((cpu.get().lower()), "Error"))

data = get_data()
button = Button(root, text="CPU Search", command=button_click)
button.grid(row=9, column=1)

root.mainloop()