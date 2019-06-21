"""
    1. Create DataBase
    2. Create Table in Database following ORM
    3. Add mysql-connector library in your program
        > Settings > > Project > Project Interpreter

"""

import mysql.connector

class Customer:

    # Constructor
    def __init__(self, name="NA", phone="NA", email="NA"):
        self.name = name
        self.phone = phone
        self.email = email


c1 = Customer()

c1.name = input("Enter Customer Name: ")
c1.phone = input("Enter Customer Phone: ")
c1.email = input("Enter Customer Email: ")


print("Choose an Option:")
print("1. Add Customer")
print("2. Update Customer")
print("3. Delete Customer")
print("4. View Customer")
print("5. View All Customers")

choice = int(input("Please Enter Your Choice: "))
if choice == 1:

    #we will code to save data in database

    # 1. Write SQL Statement
    sql = "insert into Customer values(null, '{}', '{}', '{}')".format(c1.name, c1.phone, c1.email)

    # 2. Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="localhost", database="aurigne")

    # 3. Create cursor from connection to execute sql commands : insert/update/delete and select commands
    cursor = con.cursor()
    cursor.execute(sql)

    # 4. Commit as Transaction
    con.commit() # Transaction

    print(c1.name," Saved in DataBase")


elif choice == 2:
    print("Update")

elif choice == 3:
    print("Delete")

elif choice == 4:
    sql = "select * from Customer where cid = {}".format(c1.cid)

elif choice == 5:
    # 1. Write SQL Statement
    sql = "select * from Customer"

    # 2. Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="localhost", database="aurigne")

    # 3. Create cursor from connection to execute sql commands : insert/update/delete and select commands
    cursor = con.cursor()
    cursor.execute(sql)

    # in select statements we do not commit because it is a read operation
    rows = cursor.fetchall()
    # print(rows) # list of tuples

    for row in rows:
        #print(row)
        print(row[1], row[3])


# Explore update and delete statements
