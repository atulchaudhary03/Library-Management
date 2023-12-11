from tkinter import *
from tkinter import messagebox
import mysql.connector

def delete_db():
    global id

    bid = id.get()

    db = mysql.connector.connect(host="localhost", user="root", password='Drago@22', database='db')
    cursor = db.cursor()

    print(bid, end='--')
    print("delete")

    
    check_query = "SELECT * FROM books WHERE bid='" + bid + "' AND available='YES';"
    cursor.execute(check_query)
    book = cursor.fetchone()

    if book:
        delete_query = "DELETE FROM books WHERE bid='" + bid + "';"
        print(delete_query)

        try:
            cursor.execute(delete_query)
            db.commit()
            messagebox.showinfo('Success', "Book deleted successfully")
        except:
            messagebox.showinfo("Error", "Failed to delete the book")
    else:
        messagebox.showinfo("Error", "Book with the given ID is not available or already issued")

    window.destroy()

def deleteBooks():
    global id

    window = Tk()
    window.title('Library Management System')

    greet = Label(window, font=('arial', 30, 'bold'), text="Delete Books")
    greet.grid(row=0, columnspan=3)


    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book ID: ")
    L.grid(row=2, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    submitbtn = Button(window, text="Submit", command=delete_db, bg="DodgerBlue2", fg="white",
                       font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    print("delete")
    pass
