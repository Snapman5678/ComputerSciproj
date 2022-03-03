import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import mysql.connector as sqltor
import os 
import matplotlib.pyplot as plt


root = tk.Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='white')



passwordsql = os.environ.get('SQL_PASS')

mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

if mycon.is_connected == False:
    print("Error Connecting")

cursor = mycon.cursor()
st1 = 'SELECT * FROM TEMPUSER;'
cursor.execute(st1)
data1 = cursor.fetchone()
user1 = data1[0]
st = f'SELECT * FROM USERS WHERE USERNAME = "{user1}"'
cursor.execute(st)

data = cursor.fetchone()
namepro = data[1]
vaccinepro = data[3]
boosterpro = data[4]
mycon.close()

def addvac():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st2 = f'UPDATE USERS SET VACCINE = VACCINE + 1 WHERE USERNAME = "{user1}"'
    cursor.execute(st2)
    mycon.commit()
    global vaccinepro
    st = f'SELECT * FROM USERS WHERE USERNAME = "{user1}"'
    cursor.execute(st)

    data = cursor.fetchone()
    vaccinepro = data[3]
    vacclabel.config(text = vaccinepro)
    mycon.close()
    return vaccinepro

def subvac():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st2 = f'UPDATE USERS SET VACCINE = VACCINE - 1 WHERE USERNAME = "{user1}"'
    cursor.execute(st2)
    mycon.commit()
    global vaccinepro
    st = f'SELECT * FROM USERS WHERE USERNAME = "{user1}"'
    cursor.execute(st)

    data = cursor.fetchone()
    vaccinepro = data[3]
    vacclabel.config(text = vaccinepro)
    mycon.close()
    return vaccinepro

def addboo():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st2 = f'UPDATE USERS SET BOOSTERS = BOOSTERS + 1 WHERE USERNAME = "{user1}"'
    cursor.execute(st2)
    mycon.commit()
    global boosterpro
    st = f'SELECT * FROM USERS WHERE USERNAME = "{user1}"'
    cursor.execute(st)

    data = cursor.fetchone()
    boosterpro = data[4]
    boolabel.config(text = boosterpro)
    mycon.close()
    return boosterpro

def subboo():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    if mycon.is_connected == False:
        print("Error Connecting")

    cursor = mycon.cursor()

    st2 = f'UPDATE USERS SET BOOSTERS = BOOSTERS - 1 WHERE USERNAME = "{user1}"'
    cursor.execute(st2)
    mycon.commit()
    global boosterpro
    st = f'SELECT * FROM USERS WHERE USERNAME = "{user1}"'
    cursor.execute(st)

    data = cursor.fetchone()
    boosterpro = data[4]
    boolabel.config(text = boosterpro)
    mycon.close()
    return boosterpro
#edit PROFILE

def editprofile():

    import EditProfile
#Graph Thing

def graphstats():
    passwordsql = os.environ.get('SQL_PASS')

    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = passwordsql, database ='projectc12')

    cursor = mycon.cursor()

    st = 'SELECT VACCINE, BOOSTERS FROM USERS;'

    cursor.execute(st)

    res = cursor.fetchall()

    vac = []
    boos = []

    for i in res:
        print(i[0], i[1])
        vac.append(i[0])
        boos.append(i[1])
    
    plt.scatter(boos, vac)
    plt.show()


#DISPLAYING EVERYTHING 

userdisp = tk.Label(root, text = "USERNAME:", fg = 'black', bg = 'white', font = ('Helvetica', 25))
userdisp.place(x = 50, y = 50 )
namelbl = tk.Label(root, text = namepro.upper() , bg = 'white', fg ='black', font = ('Helvetica', 25))
namelbl.place(x = 350, y = 50)

vaccdisp = tk.Label(root, text = 'VACCINES TAKEN:', fg ='black', bg = 'white', font = ('Helvetica', 25))
vaccdisp.place(x = 50, y = 100)
vacclabel = tk.Label(root, text = vaccinepro , bg = 'white', fg ='black', font = ('Helvetica', 25))
vacclabel.place(x = 390, y = 100)



boodisp = tk.Label(root, text = "BOOSTERS TAKEN:", fg = 'black', bg = 'white', font = ('Helvetica', 25))
boodisp.place(x = 50, y = 150)
boolabel = tk.Label(root, text = boosterpro , bg = 'white', fg ='black', font = ('Helvetica', 25))
boolabel.place(x = 390, y = 150)


graphbutton = tk.Button(root, text = 'SHOW STATISTICS', command = graphstats, font = ('Helvetica', 20))
graphbutton.place(x = 50, y = 300)

editpro = tk.Button(root, text = 'EDIT PROFILE', command = editprofile, font = ('Helvetica', 25))
editpro.place(x = 50, y = 400)
root.mainloop()



