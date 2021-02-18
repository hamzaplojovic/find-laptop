from pymongo import MongoClient
import tkinter
from tkinter import *
from tkhtmlview import HTMLLabel
import csv



def create_db_labels():
#Cpu Efficiency Price link

    root = Tk()
    
    root.title('Laptop Finder')

    client = MongoClient('mongodb+srv://admin:iphsgJHapeNdSWYR@cluster0.nteyj.mongodb.net', 27017)
    db = client['mydb']
    collection = db['Laptops']

    frame_header = Frame(root)
    frame_items = Frame(root)


    def list_elements(price=None):


        
        if price:
            posts = collection.find({"price":{"$lt": price}}).sort("efficiency", -1)
        else:
            posts = collection.find().sort("efficiency", -1)
    

        elements = []
        row=1
        for x in posts:
            cpu = x['cpu']
            price = x['price']
            efficiency = x['efficiency']
            link = x['link']
            
            posts_label = Label(frame_items, text=f'{cpu} - {efficiency} - {price} - ', font=("Arial", 18))
            html_label=HTMLLabel(frame_items, html=f'<a href="{link}"> LINK </a>')

            posts_label.grid(row=row, column=0)
            html_label.grid(row=row,column=1)
            html_label.fit_height()

   
            
            row += 1

        frame_items.pack()

    def filter_items():
        value = int(filter_entry.get())
        for x in frame_items.winfo_children():
            x.destroy()

        list_elements(value)
    
    #=====================================================
    filter_label = tkinter.Label(frame_header, text="Price:")
    filter_label.grid(row=0, column=0, columnspan=4)
    #=====================================================
    filter_entry = Entry(frame_header, font=('Arial', 12, 'bold'))
    filter_entry.grid(row=0, column=10, columnspan=4)
    #======================================================
    button_search = Button(frame_header, text="Search", command=filter_items)
    button_search.grid(row=0, column=20, columnspan=4)

    frame_header.pack()
    list_elements()

    root.mainloop()



create_db_labels()