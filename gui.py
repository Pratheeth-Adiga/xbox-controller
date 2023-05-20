import tkinter as tk
import sqlite3

con = sqlite3.connect('control.db')
cur = con.cursor()
a = cur.execute("SELECT * FROM profiles")
data = a.fetchone()
row = 10; col = 3
window = tk.Tk()
window.wm_title("JoyCon")

def save_data():
    global PROFILE_NAME_entry,B_entry,A_entry,X_entry,Y_entry,START_entry,BACK_entry,LJ_entry,RJ_entry,LB_entry,RB_entry,LJ_XN_entry,LJ_XP_entry,LJ_YN_entry,LJ_YP_entry,RJ_XN_entry,RJ_XP_entry,RJ_YN_entry,RJ_YP_entry,LT_entry,RT_entry,TOP_entry,BOTTOM_entry,LEFT_entry,RIGHT_entry,TOP_LEFT_entry,TOP_RIGHT_entry,BOTTOM_LEFT_entry,BOTTOM_RIGHT_entry
    PROFILE_NAME_KEY = PROFILE_NAME_entry.get()
    B_KEY = B_entry.get()
    A_KEY = A_entry.get()
    X_KEY = X_entry.get()
    Y_KEY = Y_entry.get()
    START_KEY = START_entry.get()
    BACK_KEY = BACK_entry.get()
    LJ_KEY = LJ_entry.get()
    RJ_KEY = RJ_entry.get()
    LB_KEY = LB_entry.get()
    RB_KEY = RB_entry.get()
    LJ_XN_KEY = LJ_XN_entry.get()
    LJ_XP_KEY = LJ_XP_entry.get()
    LJ_YN_KEY = LJ_YN_entry.get()
    LJ_YP_KEY = LJ_YP_entry.get()
    RJ_XN_KEY = RJ_XN_entry.get()
    RJ_XP_KEY =  RJ_XP_entry.get() 
    RJ_YN_KEY =  RJ_YN_entry.get()                   
    RJ_YP_KEY = RJ_YP_entry.get()
    LT_KEY = LT_entry.get()
    RT_KEY = RT_entry.get()
    TOP_KEY = TOP_entry.get()
    BOTTOM_KEY = BOTTOM_entry.get()
    LEFT_KEY = LEFT_entry.get()
    RIGHT_KEY = RIGHT_entry.get()
    TOP_LEFT_KEY = TOP_LEFT_entry.get()
    TOP_RIGHT_KEY = TOP_RIGHT_entry.get()
    BOTTOM_LEFT_KEY = BOTTOM_LEFT_entry.get()
    BOTTOM_RIGHT = BOTTOM_RIGHT_entry.get()

    cur.execute('''UPDATE profiles SET PROFILE_NAME = ?,
    B = ?,
    A = ?,
    X = ?,
    Y = ?,
    START = ?,
    BACK = ?,
    LJ = ?,
    RJ = ?,
    LB = ?,
    RB = ?,
    LJ_XN = ?,
    LJ_XP = ?,
    LJ_YN = ?,
    LJ_YP = ?,
    RJ_XN = ?,
    RJ_XP = ?, 
    RJ_YN = ?,             
    RJ_YP = ?,
    LT = ?,
    RT = ?,
    TOP = ?,
    BOTTOM = ?,
    LEFT = ?,
    RIGHT = ?,
    TOP_LEFT = ?,
    TOP_RIGHT = ?,
    BOTTOM_LEFT = ?,
    BOTTOM_RIGHT = ?
    ''', 
    (PROFILE_NAME_KEY ,
    B_KEY ,
    A_KEY ,
    X_KEY ,
    Y_KEY ,
    START_KEY ,
    BACK_KEY ,
    LJ_KEY ,
    RJ_KEY ,
    LB_KEY ,
    RB_KEY ,
    LJ_XN_KEY ,
    LJ_XP_KEY ,
    LJ_YN_KEY ,
    LJ_YP_KEY ,
    RJ_XN_KEY ,
    RJ_XP_KEY ,
    RJ_YN_KEY ,
    RJ_YP_KEY ,
    LT_KEY ,
    RT_KEY ,
    TOP_KEY ,
    BOTTOM_KEY ,
    LEFT_KEY ,
    RIGHT_KEY ,
    TOP_LEFT_KEY ,
    TOP_RIGHT_KEY ,
    BOTTOM_LEFT_KEY ,
    BOTTOM_RIGHT ,))
    con.commit()
    print("data save success")

i = 1; j = 1
def create_widget(label_text, default_value):
    global i,j,col,row
    label = tk.Label(window, text=label_text)
    label.grid(row = i*2 - 1, column = j, padx= 5)
    entry = tk.Entry(window)
    entry.insert(0, default_value)
    entry.grid(row = i*2, column = j, padx= 5, pady= 2)
    i = i + 1
    if(i > row):
        i = 1
        j = j + 1
    return entry

save_button = tk.Button(window, text="Save data", command=save_data)
save_button.grid(row = 0, column = int(col/2 + 1), pady = 10)


PROFILE_NAME_entry = create_widget("Enter PROFILE_NAME:",data[1])
B_entry = create_widget("Enter B:",data[2])
A_entry = create_widget("Enter A:",data[3])
X_entry = create_widget("Enter X:",data[4])
Y_entry = create_widget("Enter Y:",data[5])
START_entry = create_widget("Enter START:",data[6])
BACK_entry = create_widget("Enter BACK:",data[7])
LJ_entry = create_widget("Enter LJ:",data[8])
RJ_entry = create_widget("Enter RJ:",data[9])
LB_entry = create_widget("Enter LB:",data[10])
RB_entry = create_widget("Enter RB:",data[11])
LJ_XN_entry = create_widget("Enter LJ_XN:",data[12])
LJ_XP_entry = create_widget("Enter LJ_XP:",data[13])
LJ_YN_entry = create_widget("Enter LJ_YN:",data[14])
LJ_YP_entry = create_widget("Enter LJ_YP:",data[15])
RJ_XN_entry = create_widget("Enter RJ_XN:",data[16])
RJ_XP_entry = create_widget("Enter RJ_XP:",data[17])
RJ_YN_entry = create_widget("Enter RJ_YN:",data[18])
RJ_YP_entry = create_widget("Enter RJ_YP:",data[19])
LT_entry = create_widget("Enter LT:",data[20])
RT_entry = create_widget("Enter RT:",data[21])
TOP_entry = create_widget("Enter TOP:",data[22])
BOTTOM_entry = create_widget("Enter BOTTOM:",data[23])
LEFT_entry = create_widget("Enter LEFT:",data[24])
RIGHT_entry = create_widget("Enter RIGHT:",data[25])
TOP_LEFT_entry = create_widget("Enter TOP_LEFT:",data[26])
TOP_RIGHT_entry = create_widget("Enter TOP_RIGHT:",data[27])
BOTTOM_LEFT_entry = create_widget("Enter BOTTOM_LEFT:",data[28])
BOTTOM_RIGHT_entry = create_widget("Enter BOTTOM_RIGHT:",data[29])

window.mainloop()



