from pymongo import MongoClient
import tkinter
from tkinter import *

def create_db_labels():

    root = Tk()
    root.title('Laptop Finder')

    client = MongoClient('localhost', 27017)
    db = client['mydb']
    collection = db['Laptops']
    posts = collection.find()
    for x in posts:
        posts_label = Label(root, text=x)
        posts_label.pack()
    
    root.mainloop()


create_db_labels()
        


