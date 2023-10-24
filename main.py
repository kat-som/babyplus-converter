# IMPORTS #
import json
import xlsxwriter
from datetime import datetime
import os

from variables import *


def load_data(file_path, aspect_of_baby):
    data_json = open(file_path)
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
    '''
    creates a list of lists
    the first list contains column names
    '''
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
    # file_path = '/Users/kathy/Desktop/aNAUKA/projects/babyplus-converter/babyplus_data_export.json'

    dict_with_notes = get_details(
        file_path=file_path, aspect_of_baby=aspect_of_baby)

    create_xlsx(cols=cols, dict_with_notes=dict_with_notes,
                file_name=file_name)


run_all(cols=cols_poop,
        file_name='cc',
        file_path='/Users/kathy/Desktop/aNAUKA/projects/babyplus-converter/babyplus_data_export.json',
        aspect_of_baby='baby_nappy')
