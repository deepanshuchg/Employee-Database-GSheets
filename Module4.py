#Searching an Entry

from tkinter import Tk, Button, Label, Entry, CENTER, END
from gspread_module import setup_gs
import gspread



def search_data(search_emp_id):  
    sheet = setup_gs()                                                  #Initilize sheet object
    search_cell = sheet.find(search_emp_id)                             #This will initialize a cell object where the entry is present
    search_row = search_cell.row                                        #Initilizing row number of the entry found
    data=[sheet.cell(search_row,2).value , sheet.cell(search_row,3).value , sheet.cell(search_row,4).value, sheet.cell(search_row,5).value , sheet.cell(search_row,6).value]
    #Adding data to the data list
    return data

def search_entry():
    root1 = Tk()
    root1.title("Search Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')

    lb2= Label(root1,text="", bg = '#0084FF' ,fg="white", font="Futura 12 bold")            #This label will display confirmation message
    lb2.place(x=280,y=420)
    
    Label (root1, text ="Search Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)      #Heading
    Label(root1,text="Enter employee ID:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=200,y=200,anchor=CENTER)           #Label for text 
    user_entry = Entry (root1, width=20, bg="white")                                                                                    #Text box
    user_entry.place(x =350, y = 200, anchor = CENTER)

    def clicked():                                                              #When the button is pressed
        emp_id = user_entry.get()                                               #This will get employee id from the text box

        try:                                                                            #try-except for catching a exception if the emp id is not found in the database
            data = search_data(emp_id)
            message = f"Employee ID: {emp_id}\nFirst Name: {data[0]}\nLast Name: {data[1]}\nCity: {data[2]}\nZip: {data[3]}\nPhone number: {data[4]}" #adding the data to a message if the entry is found
        except gspread.exceptions.CellNotFound:            #This exception will occur if no entry is found in the database 
            message="No data found with that employee id"         
            
        lb2.configure(text=message)

    Button (root1, text="SEARCH", width=60, command= clicked).place(x =350, y = 300, anchor = CENTER)

    return root1.mainloop()