from tkinter import *

root = Tk()

# Define possible inputs
inputs = ["one"]

# Create a list of suggestions based on the input givenA
def suggest_input(event):
    suggestions_listbox.delete(0, END)
    input_text = input_entry.get()
    suggestions = [input for input in inputs if input.startswith(input_text)]
    for suggestion in suggestions:
        suggestions_listbox.insert(END, suggestion)

# Get the selected suggestion and display it on the input field
def get_suggestion(event):
    if suggestions_listbox.curselection():
        selected_input = suggestions_listbox.get(suggestions_listbox.curselection())
        input_entry.delete(0, END)
        input_entry.insert(0, selected_input)
        suggestions_listbox.delete(0, END)

# Create GUI elements
input_label = Label(root, text="Enter input:")
input_entry = Entry(root)
suggestions_listbox = Listbox(root, height=5)

# Bind events to the input field and suggestions listbox
input_entry.bind("<KeyRelease>", suggest_input)
suggestions_listbox.bind("<Double-Button-1>", get_suggestion)

# Arrange GUI elements
input_label.pack()
input_entry.pack()
suggestions_listbox.pack()

root.mainloop()
