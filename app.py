import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import Calendar
from main import *


def choose_file():
    file_path = filedialog.askopenfilename()
    file_label.config(text="Chosen file: " + file_path)


def run():
    # Define the action to be performed when the "Run All" button is clicked

    # run_all()
    pass


# Create a Tkinter window
window = tk.Tk()
window.title("Tkinter Components Example")

# Create a label to display the chosen file
file_label = tk.Label(window, text="Chosen file: None")
file_label.pack()

# Create a "Choose File" button
choose_file_button = tk.Button(window, text="Choose File", command=choose_file)
choose_file_button.pack()

# Create three checkboxes
checkboxes = []
for option in ["bottlefed", "breastfed", "solids", 'nappy']:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(window, text=option, variable=var)
    checkbox.pack()
    checkboxes.append((option, var))

# Create a radio button
radio_var = tk.StringVar()
radio_button = tk.Radiobutton(
    window, text="Check In", variable=radio_var, value="Check In")
radio_button.pack()


# Create a button to run all
run_all_button = tk.Button(window, text="Run", command=run)
run_all_button.pack()

# Start the Tkinter main loop
window.mainloop()

print(checkboxes)
