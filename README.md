# babyplus

This app is a companion app to the baby plus app that allows you to track your baby's progress, what he or she eats and other baby-related matters. You can download data in JSON format from the application, but data in this format is difficult to read by humans. When, for example, we go to the doctor, we sometimes need data in table format and that's why I created an application that takes data in json format and turns it into a table in Excel

https://apps.apple.com/us/app/pregnancy-tracker-app/id505864483

# Baby Tracking Data Converter

The Baby Tracking Data Converter is a simple GUI application built using Python and Tkinter. It facilitates the conversion of JSON data related to baby tracking into Excel files for easy management and analysis.

## Features

- **Load JSON Data**: The application allows users to load JSON data files containing baby tracking information.
- **Select Tracking Aspects**: Users can choose specific aspects of baby tracking data, such as milk consumption and nappy changes, for conversion into Excel files.
- **Generate Excel Files**: Upon selection, the application converts the chosen data aspects into Excel files, making it convenient for further analysis or sharing.

## Installation

Ensure you have Python installed on your system. You can install Python from the [official Python website](https://www.python.org/downloads/).

Next, install the required dependencies using pip:

```bash
pip install xlsxwriter
