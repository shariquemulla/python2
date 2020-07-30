from tkinter import *
from backend import Database

database = Database()

window = Tk()
window.wm_title("Bookstore")

id = 0
title = StringVar()
author = StringVar()
year = StringVar()
isbn = StringVar()

def view_command(books=None):
    list_box.delete(0,END)
    if books is None:
        books = database.view_all()
    for book in books:
        list_box.insert(END,book)
    
def get_selected_row(event=None):
    try:
        index = list_box.curselection()[0]
        global selected_row
        selected_row = list_box.get(index)
        entry_title.delete(0,END)
        entry_author.delete(0,END)
        entry_year.delete(0,END)
        entry_isbn.delete(0,END)
        entry_title.insert(END,selected_row[1])
        entry_author.insert(END,selected_row[2])
        entry_year.insert(END,selected_row[3])
        entry_isbn.insert(END,selected_row[4])
    except IndexError:
        pass

def search_command():
    books = database.search(title.get(),author.get(),year.get(),isbn.get())
    view_command(books)

def add_command():
    database.insert(title.get(),author.get(),year.get(),isbn.get())
    view_command()

def update_command():
    database.update(selected_row[0],title.get(),author.get(),year.get(),isbn.get())
    view_command()

def delete_command():
    database.delete(selected_row[0])
    view_command()

def close_command():
    window.destroy()

label_title = Label(window, text="Title")
label_title.grid(row=0,column=0)
label_author = Label(window, text="Author")
label_author.grid(row=0,column=2)
label_year = Label(window, text="Year")
label_year.grid(row=1,column=0)
label_isbn = Label(window, text="ISBN")
label_isbn.grid(row=1,column=2)

entry_title = Entry(window, textvariable=title)
entry_title.grid(row=0,column=1)
entry_author = Entry(window, textvariable=author)
entry_author.grid(row=0,column=3)
entry_year = Entry(window, textvariable=year)
entry_year.grid(row=1,column=1)
entry_isbn = Entry(window, textvariable=isbn)
entry_isbn.grid(row=1,column=3)

list_box = Listbox(window, width=35)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

list_box.configure(yscrollcommand=sb.set)
sb.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',get_selected_row)

button_view = Button(window,text='View All',width=12,command=view_command)
button_view.grid(row=2,column=3)
button_search = Button(window,text='Search',width=12,command=search_command)
button_search.grid(row=3,column=3)
button_add = Button(window,text='Add Entry',width=12,command=add_command)
button_add.grid(row=4,column=3)
button_update = Button(window,text='Update',width=12,command=update_command)
button_update.grid(row=5,column=3)
button_delete = Button(window,text='Delete',width=12,command=delete_command)
button_delete.grid(row=6,column=3)
button_close = Button(window,text='Close',width=12,command=close_command)
button_close.grid(row=7,column=3)

window.mainloop()