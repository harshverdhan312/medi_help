import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as db
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def submitbtn1():
    global con
    global cur

    username = name_entry.get()
    password = pass_entry.get()
    con = db.connect(host="localhost", user=username, password=password)
    cur = con.cursor()
    create_database_and_table(cur)


def submitbtn2():
    cur.execute("use medi_help")
    date = date_entry_label.get()
    print(date)
    systolic_bp = systolic_bp_entry_label.get()
    diastolic_bp = diastolic_bp_entry_label.get()
    query = "insert into medi_info values({},{},{})".format(
        date, systolic_bp, diastolic_bp)

    cur.execute(query)
    con.commit()
    con.close()
    root2.destroy()


def mainscreen():
    global root
    global name_entry
    global pass_entry

    root = tk.Tk()
    root.title("MediHelp")
    root.geometry("500x500")

    img = ImageTk.PhotoImage(Image.open("aksh-m.h.png"))
    tk.Label(root, image=img, height=250, width=240).place(x=125, y=0)

    name_label = tk.Label(text="Your Sql Username")
    name_entry = tk.Entry(root)
    pass_label = tk.Label(text="Your Sql Password")
    pass_entry = tk.Entry(root)

    name_label.place(x=50, y=200)
    name_entry.place(x=200, y=200)
    pass_label.place(x=50, y=250)
    pass_entry.place(x=200, y=250)

    submit_button = tk.Button(root, text="Submit", command=submitbtn1)
    submit_button.place(x=325, y=325)

    root.mainloop()


def create_database_and_table(cur):
    try:
        cur.execute("SHOW DATABASES;")
        result_databases = cur.fetchall()

        if ("medi_help",) not in result_databases:
            create_database_query = "CREATE DATABASE medi_help;"
            use_database_query = "USE medi_help"
            create_table_query = "CREATE TABLE medi_info (DATE VARCHAR(255) NOT NULL, SYSTOLIC_BP INT NOT NULL, DIASTOLIC_BP INT NOT NULL);"

            list_query = [create_database_query,
                          use_database_query, create_table_query]

            for query in list_query:
                cur.execute(query)
                print("done")
    except db.Error as err:
        print(f"Error: {err}")
    finally:

        print("moving to next screen")
        root.destroy()
        homescreen()


def homescreen():
    global root2
    global systolic_bp_entry_label
    global diastolic_bp_entry_label
    global date_entry_label

    root2 = tk.Tk()
    root2.title("MediHelp")
    root2.geometry("500x500")

    img = ImageTk.PhotoImage(Image.open("aksh-m.h.png"))
    tk.Label(root2, image=img, height=250, width=240).place(x=125, y=0)

    date_label = tk.Label(text="Enter today date")
    systolic_bp_label = tk.Label(text="Enter your SYStolic BLood Pressure ")
    diastolic_bp_label = tk.Label(text="Enter your DIAStolic BLood Pressure ")
    date_entry_label = tk.Entry(root2)
    systolic_bp_entry_label = tk.Entry(root2)
    diastolic_bp_entry_label = tk.Entry(root2)

    date_label.place(x=50, y=200)
    date_entry_label.place(x=300, y=200)
    systolic_bp_label.place(x=50, y=250)
    systolic_bp_entry_label.place(x=300, y=250)
    diastolic_bp_label.place(x=50, y=300)
    diastolic_bp_entry_label.place(x=300, y=300)

    submit_button = tk.Button(root2, text="Submit", command=submitbtn2)
    submit_button.place(x=325, y=325)

    root2.mainloop()


mainscreen()
