#Adding item

from tkinter import Tk, Button, Label, Entry, CENTER, END
from gspread_module import setup_gs

def add_data(first_name,last_name,state,zip,phone):  
    sheet = setup_gs()                                                  #Initilize sheet object
    data = sheet.get_all_records()                                      #This will be use to count total rows in the sheet
    max_row = len(data)                                                 #This will give total rows - top row
    emp_id = int(sheet.cell( max_row + 1 , 1).value)                    #Will find the last employee ID              
    list = [emp_id + 1, first_name, last_name, state, zip, phone]       #Will add all the details in a list with incrementing the employee ID

    for i in range(1,7):                                                #For loop for adding the values seprately   
        sheet.update_cell(max_row + 2,i,list[i-1])


def new_entry():
    root1 = Tk()
    root1.title("New Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')

    lb1= Label (root1, text ="New Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold")            #Heading
    lb1.place(x =350, y = 100, anchor = CENTER)

    lb2= Label(root1,text="", bg = '#0084FF' ,fg="white", font="Futura 20 bold")            #This label will display message when the data is added succesfully
    lb2.place(x=200,y=420)

    Label(root1,text="First Name:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=230,y=200,anchor=CENTER)      #Label for text "First Name"
    fname_entry = Entry(root1, width=20, bg="white")                                                                        #Text box for First Name
    fname_entry.place(x =360, y = 200, anchor = CENTER)

    Label(root1,text="Last Name:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=230,y=230,anchor=CENTER)
    lname_entry = Entry(root1, width=20, bg="white")
    lname_entry.place(x =360, y = 230, anchor = CENTER)

    Label(root1,text="State:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=230,y=260,anchor=CENTER)
    state_entry = Entry(root1, width=20, bg="white")
    state_entry.place(x =360, y = 260, anchor = CENTER)

    Label(root1,text="Zip Code:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=230,y=290,anchor=CENTER)
    zip_entry = Entry(root1, width=20, bg="white")
    zip_entry.place(x =360, y = 290, anchor = CENTER)

    Label(root1,text="Phone Number:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=230,y=320,anchor=CENTER)
    phone_entry = Entry(root1, width=20, bg="white")
    phone_entry.insert(0,"999-999-9999")                            #Putting the format in which phone number is to be added. Tkinter doesn't support placeholder
    phone_entry.place(x =360, y = 320, anchor = CENTER)

    def clicked():
        first_name = fname_entry.get()                           #This section takes the input values from the text boxes
        last_name = lname_entry.get()
        state = state_entry.get()
        zip = zip_entry.get()
        phone = phone_entry.get()

        zip_entry.delete(0, END)
        phone_entry.delete(0, END)
        fname_entry.delete(0, END)                               #Clear the values of the text boxes   
        lname_entry.delete(0, END)
        state_entry.delete(0, END)

        add_data(first_name,last_name,state,int(zip),phone)        #Call the function to add values

        lb2.configure(text= "Entry added!")                         #Setting up confirmation message
        

    Button (root1, text="Press to add a new Entry", width=60, command = clicked).place(x =350, y = 390, anchor = CENTER)            #Button object

    return root1.mainloop()        