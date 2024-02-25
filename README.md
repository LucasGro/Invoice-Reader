# Invoice Reader

This script is designed to read specific data from a set of invoices. The data to be extracted includes the following:

- Invoice #
- Date
- File name

## Usage

1. **Ensure Python is installed** on your system. If not, download and install it from the [official Python website](https://www.python.org/).

2. **Install the required Python packages**: `openpyxl`, `pdfminer.six`, and `pandas`. You can install them using pip with the following command:
   
   pip install openpyxl pdfminer.six pandas


3. **Clone this repository** to your local machine or download the script `__main__.py` directly.

4. **Place the invoices** that you want to process in the "input" folder within the repository directory or use already attached.

5. **Run the script** by executing the command: `python __main__.py`.

6. The script will read the specified data from the invoices in the "input" folder and generate a report.

## Summary of Resolution

The script successfully reads the required data (Invoice #, Date, and File name) from the invoices. It utilizes the `pdfminer.six` library to extract text from PDF files, `openpyxl` to write the extracted data to an Excel file, and `pandas` for data manipulation and analysis.

For any questions or assistance, please contact me.

Thank you!
