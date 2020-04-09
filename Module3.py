#Deleting Entry

from tkinter import Tk, Button, Label, Entry, CENTER, END
from gspread_module import setup_gs
import gspread

def del_data(del_emp_id):
    sheet = setup_gs()                                                  #Initilize sheet object
    d_cell = sheet.find(del_emp_id)                                     #This will initialize a cell object where the entry is present
    #If no entry is found, it will throw an exception
    d_row = d_cell.row                                                  #Initilizing row number of the entry found
    sheet.delete_row(d_row)                                             #This will delete the row

def delete_entry():
    root1 = Tk()
    root1.title("Delete Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')
    
    Label (root1, text ="Delete Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)      #Heading

    lb2= Label(root1,text="", bg = '#0084FF' ,fg="white", font="Futura 12 bold")            #This label will display confirmation message
    lb2.place(x=280,y=420)

    Label(root1,text="Enter employee ID:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=200,y=200,anchor=CENTER)       #Text "Enter Employee ID"
    user_entry = Entry (root1, width=20, bg="white")                                                                                #Text box
    user_entry.place(x =350, y = 200, anchor = CENTER)

    def clicked():
        emp_id = user_entry.get()                     #This will get the data from the text box
        try:
            del_data(emp_id)                    #Calling del function which will return a message based on entry is found or not
            message="Entry deleted"
            lb2.configure(text=message)
        except gspread.exceptions.CellNotFound:            #This exception will occur if no entry is found in the database 
            message="No data found with that employee id"
            lb2.configure(text=message)     

    Button (root1, text="DELETE", width=60,command=clicked).place(x =350, y = 300, anchor = CENTER)
    return root1.mainloop()