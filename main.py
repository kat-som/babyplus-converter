import tkinter as tk
from tkinter import filedialog
import json
import xlsxwriter
from datetime import datetime
import os

from variables import *

#  Functions


def load_data(file_path, aspect_of_baby):
    with open(file_path, 'r') as data_json:
        data_dict = json.load(data_json)

    details_dict = data_dict['tracker_detail']
    main_dict = data_dict[f'{aspect_of_baby}']

    return details_dict, main_dict


def get_details(file_path, aspect_of_baby):
    details_dict, main_dict = load_data(
        file_path=file_path, aspect_of_baby=aspect_of_baby)

    for d_main in main_dict:
        d_main['date'] = datetime.fromtimestamp(
            d_main['date']).strftime('%d/%m/%Y, %H:%M:%S')
        for dict_trackerdetail in details_dict:
            if dict_trackerdetail['trackerType'] == 11 and dict_trackerdetail['trackerDetailId'] == d_main['pk']:
                d_main['note'] = dict_trackerdetail['trackerDescription']
                break
        else:
            d_main['note'] = 'no note'

    dict_with_notes = main_dict
    return dict_with_notes


def create_list_of_lists(cols, dict_with_notes):
    list_of_cols = [cols]
    for i in dict_with_notes:
        list_of_cols.append(list(i.values()))
    return list_of_cols


def create_xlsx(cols, dict_with_notes, file_name):
    cwd = os.getcwd()
    path = cwd + '/' + file_name

    workbook = xlsxwriter.Workbook(r'{}.xlsx'.format(path))
    worksheet = workbook.add_worksheet()

    lists = create_list_of_lists(cols, dict_with_notes)

    for row_num, item_list in enumerate(lists):
        for element_num, item in enumerate(item_list):
            worksheet.write(row_num, element_num, item)

    workbook.close()


def run_all(cols, file_name, file_path, aspect_of_baby):
    dict_with_notes = get_details(
        file_path=file_path, aspect_of_baby=aspect_of_baby)

    create_xlsx(cols=cols, dict_with_notes=dict_with_notes,
                file_name=file_name)


# Initialize 'file' variable globally
file = None

# tkinter GUI
# Tkinter window
window = tk.Tk()
window.title("Simple converter app for Babyplus")
window.geometry("700x350")

# chosen file
file_label = tk.Label(window, text="Chosen file: None")
file_label.pack()


def choose_file():
    global file
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        file_label.config(text="Chosen file: " + file_path)
        file = file_path
    else:
        print("No file selected.")


def run():
    global file
    global checkboxes

    if file:
        chosen_aspects = [checkbox[0]
                          for checkbox in checkboxes if checkbox[1].get()]
        if chosen_aspects:
            for aspect in chosen_aspects:
                if aspect == 'nappy':
                    run_all(cols=cols_poop, file_name='output',
                            file_path=file, aspect_of_baby='baby_nappy')
                elif aspect == 'milk':
                    run_all(cols=cols_bootlefeed, file_name='output_milk',
                            file_path=file, aspect_of_baby='baby_bottlefeed')

        else:
            print("Please select an aspect to create the Excel file for.")
    else:
        print("Please choose a file first.")


# Choose File button
choose_file_button = tk.Button(window, text="Choose File", command=choose_file)
choose_file_button.pack()

# Checkboxes
checkboxes = []
for option in ["milk", 'nappy']:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(window, text=option, variable=var)
    checkbox.pack()
    checkboxes.append((option, var))

# Button run all
run_all_button = tk.Button(window, text="Create Excel File", command=run)
run_all_button.pack()


window.mainloop()
