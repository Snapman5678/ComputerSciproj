import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk
from tkinter import *
import mysql.connector as sqltor
import os


def start():
    root.destroy()
    import Login

def adduser():
    usr = Username.get()
    passw = password.get()
    vacc = vacctaken.get()
    boos = bootaken.get()

    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st = 'SELECT * FROM USERS;'

    cursor.execute(st)
    res = cursor.fetchall()
    if len(res) > 0:
        for i in res:
            if i[1] == usr.lower():
                err1 = tk.Label(root, text = "Username already in use", fg = 'red')
                err1.place(x = 200, y = 250)
                break
            else:
                st1 = f'INSERT INTO USERS VALUES({len(res)},"{usr}","{passw}",{vacc}, {boos});'
                g1 = tk.Label(root, text = "Success!", fg = 'green')
                g1.place( x = 200, y = 250)
                cursor.execute(st1)
                cursor = mycon.cursor()
                st1 = 'DROP TABLE TEMPUSER;'
                st2 = 'CREATE TABLE TEMPUSER(Username varchar(20));'
                st3 = f'INSERT INTO TEMPUSER VALUES("{usr}");'
                cursor.execute(st1)
                cursor.execute(st2)
                cursor.execute(st3)
                mycon.commit()
                mycon.close()
                start()
    else:
        st1 = f'INSERT INTO USERS VALUES({len(res)},"{usr}","{passw}",{vacc}, {boos});'
        g1 = tk.Label(root, text = "Success!", fg = 'green')
        g1.place( x = 200, y = 250)
        cursor.execute(st1)
        cursor = mycon.cursor()
        st1 = 'DROP TABLE TEMPUSER;'
        st2 = 'CREATE TABLE TEMPUSER(Username varchar(20));'
        st3 = f'INSERT INTO TEMPUSER VALUES("{usr}");'
        cursor.execute(st1)
        cursor.execute(st2)
        cursor.execute(st3)
        mycon.commit()
        mycon.close()
        start()

    mycon.close()

root = tk.Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='white')

lblfrstrow = tk.Label(root, text = "USERNAME:", bg = 'white', fg = 'black')
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35, bg = 'white', fg = 'black')
Username.place(x = 300, y = 20, width = 100)

lblsecrow = tk.Label(root, text = "PASSWORD:", bg = 'white', fg ='black')
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35, bg = 'white', fg ='black', show = '*')
password.place(x = 300, y = 50, width = 100)

lblthrow = tk.Label(root, text = "VACCINES TAKEN:", bg = 'white', fg ='black')
lblthrow.place(x = 50, y = 80)

vacctaken = tk.Entry(root, width = 5, bg = 'white', fg ='black')
vacctaken.place(x = 300, y = 80)

lblfourth = tk.Label(root, text = "BOOSTERS TAKEN:", bg = 'white', fg ='black')
lblfourth.place(x = 50, y = 110)

bootaken = tk.Entry(root, width = 5, bg = 'white', fg = 'black')
bootaken.place(x = 300, y = 110)

submitbtn = tk.Button(root, text ="Sign Up!", command = adduser, bg = 'white')
submitbtn.place(x = 200, y = 170, width = 60)

root.mainloop()
