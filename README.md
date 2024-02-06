
# Baby Tracking Data Converter
The Baby Tracking Data Converter is a simple GUI application built using Python and Tkinter. It facilitates the conversion of JSON data from mobile app related to baby's development (food, weight etc.) into Excel files for easy management and analysis.


Baby+ app in AppStore
https://apps.apple.com/us/app/pregnancy-tracker-app/id505864483

## Features

- **Load JSON Data**: The application allows users to load JSON data files containing baby tracking information.
- **Select Tracking Aspects**: Users can choose specific aspects of baby tracking data, such as milk consumption and nappy changes, for conversion into Excel files.
- **Generate Excel Files**: Upon selection, the application converts the chosen data aspects into Excel files, making it convenient for further analysis or sharing.

## Installation

Ensure you have Python installed on your system. You can install Python from the [official Python website](https://www.python.org/downloads/).

Next, install the required dependencies using pip:

```bash
pip install xlsxwriter
```

## Usage
Run the script baby_tracking_converter.py using a Python interpreter.

The GUI window will appear.

Click the "Choose File" button to select a JSON data file containing baby tracking information.

Select the aspects of baby tracking data you want to include by checking the corresponding checkboxes.

Click the "Create Excel File" button to generate Excel files based on the selected aspects.



## File Structure
baby_tracking_converter.py: Main Python script containing the application logic.
variables.py: Module containing variables used in the main script.
README.md: Documentation file providing information about the application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
