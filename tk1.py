import tkinter as tk

data = []

def save_data():
    top_key = top_entry.get()
    bottom_key = bottom_entry.get()
    left_key = left_entry.get()
    right_key = right_entry.get()

    data.append(top_key)
    data.append(bottom_key)
    data.append(left_key)
    data.append(right_key)

    print("Data saved:", data)

window = tk.Tk()

top_label = tk.Label(window, text="Enter TOP:")
top_label.pack()

top_entry = tk.Entry(window)
top_entry.pack()

bottom_label = tk.Label(window, text="Enter BOTTOM:")
bottom_label.pack()

bottom_entry = tk.Entry(window)
bottom_entry.pack()

left_label = tk.Label(window, text="Enter LEFT:")
left_label.pack()

left_entry = tk.Entry(window)
left_entry.pack()

right_label = tk.Label(window, text="Enter RIGHT:")
right_label.pack()

right_entry = tk.Entry(window)
right_entry.pack()

save_button = tk.Button(window, text="Save data", command=save_data)
save_button.pack()

window.mainloop()