
# Import tkinter module
import tkinter as tk
import datetime
# Import Diary class from tk_diarygui.py
from pydary import Diary

# Create a root window
root = tk.Tk()

# Create a Diary object with no arguments
diary = Diary()

# Create a label for the title
title_label = tk.Label(root, text="Title:")

# Create an entry for the title
title_entry = tk.Entry(root)

# Create a label for the text
text_label = tk.Label(root, text="Text:")

# Create a text widget for the text
text_widget = tk.Text(root)

# Create a button for adding a new diary entry
add_button = tk.Button(root, text="Add", command=lambda: diary.add_entry(title_entry.get(), text_widget.get("1.0", "end")))

# Create a button for listing all the diary entries
list_button = tk.Button(root, text="List", command=lambda: show_entries("all"))

# Create a button for listing today's diary entries
today_button = tk.Button(root, text="Today", command=lambda: show_entries("today"))

# Create a button for creating an html file with all the diary entries
html_button = tk.Button(root, text="HTML", command=diary.create_html)

# Create a listbox for showing the diary entries
listbox = tk.Listbox(root)

# Place the widgets on a grid layout
title_label.grid(row=0, column=0, sticky="e")
title_entry.grid(row=0, column=1, columnspan=3, sticky="ew")
text_label.grid(row=1, column=0, sticky="ne")
text_widget.grid(row=1, column=1, columnspan=3, rowspan=3, sticky="nsew")
add_button.grid(row=4, column=0)
list_button.grid(row=4, column=1)
today_button.grid(row=4, column=2)
html_button.grid(row=4, column=3)
listbox.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Make the window resizable
root.rowconfigure(1, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(1, weight=1)

# Define a function that shows the diary entries in the listbox based on a given mode
def show_entries(mode):
    # Clear the listbox
    listbox.delete(0, "end")

    # Query all the diary entries from the table
    diary.cur.execute("SELECT * FROM entries")

    # Fetch all the rows from the query result
    rows = diary.cur.fetchall()

    # Get today's date as a string
    today = datetime.date.today().strftime("%Y-%m-%d")

    # Loop through each row and check its date based on the mode
    for row in rows:
        # If the mode is "all", then add the row to the listbox
        if mode == "all":
            listbox.insert("end", f"ID: {row[0]}")
            listbox.insert("end", f"Title: {row[1]}")
            listbox.insert("end", f"Text: {row[2]}")
            listbox.insert("end", f"Date: {row[3]}")
            listbox.insert("end", "-" * 20)

        # If the mode is "today" and the date matches today's date, then add the row to the listbox
        elif mode == "today" and row[3].startswith(today):
            listbox.insert("end", f"ID: {row[0]}")
            listbox.insert("end", f"Title: {row[1]}")
            listbox.insert("end", f"Text: {row[2]}")
            listbox.insert("end", f"Date: {row[3]}")
            listbox.insert("end", "-" * 20)

# Start the main loop of the window
root.mainloop()
