from tkinter import *
from tkinter import messagebox
import mysql.connector
import datetime

def issue_db():
    global id
    global StudentName

    bid = id.get()
    bStudentName = StudentName.get()

    db = mysql.connector.connect(host="localhost", user="root", password='Drago@22', database='db')
    cursor = db.cursor()

    print(bid, end='--')
    print(bStudentName, end='--')
    print("issue")

    try:
        checkavailability = "SELECT * FROM books WHERE available='YES' AND bid='" + bid + "';"
        print(checkavailability)
        cursor.execute(checkavailability)

        book = cursor.fetchone()

        if book:
            updatequery = "UPDATE books SET available='NO' WHERE bid='" + bid + "';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            current_date = datetime.date.today()
            sqlquery = "INSERT INTO issue VALUES('" + bid + "','" + bStudentName + "','" + str(current_date) + "');"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success', "Book issued successfully")
        else:
            messagebox.showinfo("Error", "Required book is not available")
    except:
        messagebox.showinfo("Error", "Cannot issue the given book")

def issueBooks():
    global id
    global StudentName

    window = Tk()
    window.title('Library Management System')

    greet = Label(window, font=('arial', 30, 'bold'), text="Issue Books")
    greet.grid(row=0, columnspan=3)

   

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book ID: ")
    L.grid(row=2, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Student Name: ")
    L.grid(row=4, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=4, column=2)

    StudentName = Entry(window, width=5, font=('arial', 15, 'bold'))
    StudentName.grid(row=4, column=3)

    submitbtn = Button(window, text="Submit", command=issue_db, bg="DodgerBlue2", fg="white",
                       font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    print("issue")
    pass
