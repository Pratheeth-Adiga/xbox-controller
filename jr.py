import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect('control.db')
cur = con.cursor()
a = cur.execute("SELECT * FROM profiles")
data = a.fetchone()
row = 10; col = 3
window = tk.Tk()
window.wm_title("JoyCon")
sugg_data = ['screenshot','mouseMove','brightnessIncrease','brightnessDecrease']
no_of_suggestion = 5

def save_data():
    global PROFILE_NAME_entry,B_entry,A_entry,X_entry,Y_entry
    PROFILE_NAME_KEY = PROFILE_NAME_entry.get()
    B_KEY = B_entry.get()
    A_KEY = A_entry.get()
    X_KEY = X_entry.get()
    Y_KEY = Y_entry.get()

    cur.execute('''UPDATE profiles SET PROFILE_NAME = ?,
    B = ?,
    A = ?,
    X = ?,
    Y = ?,
    ''', 
    (PROFILE_NAME_KEY ,
    B_KEY ,
    A_KEY ,
    X_KEY ,
    Y_KEY ,
))
    con.commit()
    print("data save success")

def suggest_input(event):
    current_widget = window.focus_get()
    suggestions_dropdown = dropdown_dict[current_widget]
    suggestions_dropdown['values'] = [] # clear previous suggestions
    
    input_text = input_entry.get()
    suggestions = [suggs for suggs in sugg_data if suggs.startswith(input_text)]
    suggestions_dropdown['values'] = suggestions

def get_suggestion(event):
    current_widget = window.focus_get()
    suggestions_dropdown = dropdown_dict[current_widget]
    if suggestions_dropdown.current() >= 0:
        selected_input = suggestions_dropdown.get()
        current_widget.delete(0, END)
        current_widget.insert(0, selected_input)
        suggestions_dropdown['values'] = []

i = 1; j = 1
def create_widget(label_text, default_value):
    global i, j, row, col
    label = tk.Label(window, text=label_text)
    entry = tk.Entry(window)
    entry.insert(0, default_value)
    entry.bind("<KeyRelease>", suggest_input)
    entry.bind("<FocusIn>", suggest_input) # update suggestions on focus
    entry.bind("<Return>", get_suggestion) # select suggestion on pressing enter
    label.grid(row = i*2 - 1, column = j, padx= 5)
    entry.grid(row = i*2, column = j, padx= 5, pady= 2)
    
    # create dropdown for current widget
    suggestions_dropdown = ttk.Combobox(window, height=no_of_suggestion)
    suggestions_dropdown.bind("<<ComboboxSelected>>", get_suggestion) # select suggestion on dropdown selection
    suggestions_dropdown.grid(row=i*2, column=j+1, padx=5, pady=2)
    dropdown_dict[entry] = suggestions_dropdown
    
    i += 1
    if i > row:
        i = 1
        j += 2 # increase column by 2 to accomodate dropdown
    return entry

# initialize dropdown dictionary
dropdown_dict = {'B_entry':'mouseMove','brightnessIncrease':'brightnessDecrease'}


save_button = tk.Button(window, text="Save data", command=save_data)
save_button.grid(row = 0, column = int(col/2 + 1), pady = 10)


PROFILE_NAME_KEY_entry = create_widget("Enter PROFILE_NAME:",data[1])
B_KEY_entry = create_widget("Enter B:",data[2])
A_KEY_entry = create_widget("Enter A:",data[3])
X_KEY_entry = create_widget("Enter X:",data[4])
Y_KEY_entry = create_widget("Enter Y:",data[5])

window.mainloop()



