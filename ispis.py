from pymongo import MongoClient
import tkinter
from tkinter import *
from tkhtmlview import HTMLLabel
import main

row=1
def create_db_labels():
#Cpu Efficiency Price link
    global row
    root = Tk()
    root.title('Laptop Finder')

    client = MongoClient('localhost', 27017)
    db = client['mydb']
    collection = db['Laptops']
    posts = collection.find({'price':200}).sort("efficiency", -1)
    #=====================================================
    filter_label = tkinter.Button(root, text="Price:")
    filter_label.grid(row=0, column=0, columnspan=4)
    #=====================================================
    filter_entry = Entry(root, font=('Arial', 12, 'bold'))
    filter_entry.grid(row=0, column=1, columnspan=4)
    #======================================================
    button_search = Button(root, text="Search")
    button_search.grid(row=0, column=2, columnspan=4)

    for x in posts:
        cpu = x['cpu']
        price = x['price']
        efficiency = x['efficiency']
        link = x['link']
        posts_label = Label(root, text=f'{cpu} - {efficiency} - {price} - ', font=("Arial", 18))
        html_label=HTMLLabel(root, html=f'<a href="{link}"> LINK </a>')

        posts_label.grid(row=row, column=0)
        html_label.grid(row=row,column=1)
        html_label.fit_height()

        row += 1

    root.mainloop()



create_db_labels()
        


