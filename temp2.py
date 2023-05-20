import tkinter as tk
import sqlite3

con = sqlite3.connect('control.db')
cur = con.cursor()
cur.execute("SELECT * FROM profiles")
data = cur.fetchall()

def save_data():
    global PROFILE_NAME_entry,B_entry,A_entry,X_entry,Y_entry,START_entry,BACK_entry,LJ_entry,RJ_entry
    PROFILE_NAME_KEY = PROFILE_NAME_entry.get()
    B_KEY = B_entry.get()
    A_KEY = A_entry.get()
    X_KEY = X_entry.get()
    Y_KEY = Y_entry.get()
    START_KEY = START_entry.get()
    BACK_KEY = BACK_entry.get()
    LJ_KEY = LJ_entry.get()
    RJ_KEY = RJ_entry.get()

    cur.execute('''UPDATE profiles SET PROFILE_NAME = ?,
    B = ?,
    A = ?,
    X = ?,
    Y = ?,
    START = ?,
    BACK = ?,
    LJ = ?,
    RJ = ?''', 
    (PROFILE_NAME_KEY ,
    B_KEY ,
    A_KEY ,
    X_KEY ,
    Y_KEY ,
    START_KEY ,
    BACK_KEY ,
    LJ_KEY ,
    RJ_KEY
    ))
    con.commit()

window = tk.Tk()

save_button = tk.Button(window, text="Save data", command=save_data)
save_button.pack()

def create_widget(label_text, default_value):
    label = tk.Label(window, text=label_text)
    label.pack()
    entry = tk.Entry(window)
    entry.insert(0, default_value)
    entry.pack()
    return entry

PROFILE_NAME_entry = create_widget("Enter PROFILE_NAME:",data[0][1])
B_entry = create_widget("Enter B:",data[0][2])
A_entry = create_widget("Enter A:",data[0][3])
X_entry = create_widget("Enter X:",data[0][4])
Y_entry = create_widget("Enter Y:",data[0][5])
START_entry = create_widget("Enter START:",data[0][6])
BACK_entry = create_widget("Enter BACK:",data[0][7])
LJ_entry = create_widget("Enter LJ:",data[0][8])
RJ_entry = create_widget("Enter RJ:",data[0][9])

window.mainloop()
