# IMPORTS
import json
import xlsxwriter

data_json = open(
    '/Users/kathy/Desktop/aNAUKA/projects/babyplus-converter/babyplus_data_export.json')

data_dict = json.load(data_json)


# print(data_dict['baby_bottlefeed'][-1]['pk'])

# print(data_dict['tracker_detail'],  data_dict['tracker_detail']['trackerDetailId']=491)
# print(next(
#    (item.get('trackerDescription') for item in data_dict['tracker_detail'] if item["trackerDetailId"] == 491), False))

# EXPORT FEEDINGS INTO EXCEL
# get feedings

def get_all_feedings():
    feedings_list = [["pk",
                      "amountML",
                      "isFormula",
                      "babyid",
                      "date"]]
    for i in data_dict['baby_bottlefeed'][:3]:
        feedings_list.append(list(i.values()))

    return feedings_list


# export to excel
workbook = xlsxwriter.Workbook(
    r'/Users/kathy/Desktop/aNAUKA/projects/babyplus-converter/data_from_babyplus.xlsx')
worksheet = workbook.add_worksheet()

feedings = get_all_feedings()[:2]

print(feedings)
for row_num, item_list in enumerate(feedings):
    for element_num, item in enumerate(item_list):
        worksheet.write(row_num, element_num, item)

workbook.close()
