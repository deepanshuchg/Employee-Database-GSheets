from tkinter import Tk, Button, Label, Entry, CENTER
from Module2 import new_entry
from Module3 import delete_entry
from Module4 import search_entry
from gspread_module import setup_gs
#module1--Main Screen
#contains main screen ui




def mainInstance():

    root = Tk()
    root.title("Employee Database")
    root.geometry('700x600')
    root.configure(background ='#0084FF')
    
    Label (root, text = "Welcome to Employee DataBase!", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)

    Button(root, text = "NEW ENTRY", width=10,command = new_entry).place(x =200, y =200, anchor = "e") 

    Button(root, text = "DELETE", width=10, command=delete_entry).place(x =350, y =200, anchor = CENTER) 

    Button(root, text = "SEARCH", width=10, command=search_entry).place(x =600, y =200, anchor = "e") 

    return root.mainloop()

#Program starts from here
main_screen = mainInstance()