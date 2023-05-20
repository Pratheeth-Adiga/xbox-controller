import tkinter as tk
import sqlite3

con = sqlite3.connect('control.db')
cur = con.cursor()
a = cur.execute("SELECT * FROM profiles")
data = a.fetchone()

def save_data():
    top_key = top_entry.get()
    bottom_key = bottom_entry.get()
    left_key = left_entry.get()
    right_key = right_entry.get()

    cur.execute("UPDATE profiles SET top_key = ?, bottom_key = ?, left_key = ?, right_key = ?", (top_key, bottom_key, left_key, right_key))
    con.commit()

    print("Data saved:", top_key, bottom_key, left_key, right_key)

window = tk.Tk()

top_label = tk.Label(window, text="Enter TOP:")
top_label.pack()

top_entry = tk.Entry(window)
top_entry.insert(0, data[0])
top_entry.pack()

bottom_label = tk.Label(window, text="Enter BOTTOM:")
bottom_label.pack()

bottom_entry = tk.Entry(window)
bottom_entry.insert(0, data[1])
bottom_entry.pack()

left_label = tk.Label(window, text="Enter LEFT:")
left_label.pack()

left_entry = tk.Entry(window)
left_entry.insert(0, data[2])
left_entry.pack()

right_label = tk.Label(window, text="Enter RIGHT:")
right_label.pack()

right_entry = tk.Entry(window)
right_entry.insert(0, data[3])
right_entry.pack()

save_button = tk.Button(window, text="Save data", command=save_data)
save_button.pack()

window.mainloop()

def create_widget(label_text, default_value):
    # create label widget
    label = tk.Label(window, text=label_text)
    label.pack()

    # create entry widget
    entry = tk.Entry(window)
    entry.insert(0, default_value)
    entry.pack()

    return entry  # return the entry widget


# example usage for the first two elements
top_entry = create_widget("Enter TOP:", data[0])
bottom_entry = create_widget("Enter BOTTOM:", data[1])

# example usage for another 30 elements
for i in range(2, 32):
    create_widget(f"Enter ELEMENT {i}:", data[i])

