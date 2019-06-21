from tkinter import * # GUI

import mysql.connector

def onClick():
    # print("Wow...")

    name = entryName.get()
    phone = entryPhone.get()
    email = entryEmail.get()

    print(name, phone, email)

    # 1. Write SQL Statement
    sql = "insert into Customer values(null, '{}', '{}', '{}')".format(name, phone, email)

    # 2. Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="localhost", database="aurigne")

    # 3. Create cursor from connection to execute sql commands : insert/update/delete and select commands
    cursor = con.cursor()
    cursor.execute(sql)

    # 4. Commit as Transaction
    con.commit() # Transaction

    print(name," Saved in DataBase")

window = Tk()

lblTitle = Label(window, text="Add Customer")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnSave = Button(window, text="Save Customer", command=onClick)
btnSave.pack()

window.mainloop()