import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk
from tkinter import *
import PIL.Image as img
import mysql.connector as sqltor
import os


root = tk.Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='white')


def mainnext():
    root.destroy()
    import Login




progress = Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate', )

def signuptact():
    root.destroy()
    import signup


def submitact():
    global user1
    user1 = Username.get()
    passw = password.get()
    add_tab()


    logintodb(user1, passw)


def logintodb(user, passw):
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st = 'SELECT * FROM USERS;'

    cursor.execute(st)
    usrs = cursor.fetchall()
    if len(usrs) == 0:
        errnouser = tk.Label(root, text = 'Username or password is incorrect', fg = 'red', bg = 'white')
        errnouser.place(x = 150, y = 100)

    for usr in usrs:
        if usr[1] == user and usr[2] == passw:
            mainnext()
        else:
            errnouser = tk.Label(root, text = 'Username or password is incorrect', fg = 'red', bg = 'black')
            errnouser.place(x = 150, y = 100)


lblfrstrow = tk.Label(root, text = "Username:", bg = 'white', fg = 'black')
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35, bg = 'white' , fg ='black')
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text = "Password:", bg = 'white', fg ='black')
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35, bg = 'white', fg ='black', show = '*')
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login", command = submitact, bg = 'white')
submitbtn.place(x = 150, y = 135, width = 60)

signupbtn = tk.Button(root, text ="Sign Up", command = signuptact, bg = 'white').place(x = 150, y = 165, width = 60)

def add_tab():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()
    st1 = 'DROP TABLE TEMPUSER;'
    st2 = 'CREATE TABLE TEMPUSER(Username varchar(20));'
    st3 = f'INSERT INTO TEMPUSER VALUES("{user1}");'
    cursor.execute(st1)
    cursor.execute(st2)
    cursor.execute(st3)
    mycon.commit()
    mycon.close()

root.mainloop()



