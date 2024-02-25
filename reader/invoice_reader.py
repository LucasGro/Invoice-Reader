from logger.tools import Logger
from pdfminer.high_level import extract_text
import re

log = Logger()


class InvoiceReader:
    """Reading required date from  Invoice PDF"""
    def __init__(self, path, list_of_dicts):
        try:
            self.path = path
            self.merged_dict = {}
            self.list_of_dicts = list_of_dicts
            self.invoice_date = {}
            self.invoice_name = {}
            self.invoice_number = {}

        except Exception as err:
            log.general.error(f'Extractor was not initialized. {err}')

    def pdf_text_extractor(self):
        extracted_text = extract_text(self.path)
        return extracted_text

    def number_extractor(self):
        patter = r'INVOICE #(\d+)'
        extracted_text = self.pdf_text_extractor()

        matches = re.findall(patter, extracted_text)
        for match in matches:
            self.invoice_number['#'] = match
            # print(match)
        return self.invoice_number

    def date_extractor(self):
        pattern = r'DATE: (\d{2}/\d{2}/\d{4})'
        extracted_text = self.pdf_text_extractor()

        matches = re.findall(pattern, extracted_text)
        for match in matches:
            self.invoice_date["Date"] = match

        return self.invoice_date

    def name_extractor(self):
        patter = r'^\.\/input\/(.*)\.pdf$'
        matches = re.findall(patter, self.path)
        for match in matches:
            self.invoice_name["File Name"] = match

        return self.invoice_name

    def merge_results(self):
        self.merged_dict.update(self.invoice_date)
        self.merged_dict.update(self.invoice_number)
        self.merged_dict.update(self.invoice_name)
        self.list_of_dicts.append(self.merged_dict)
        return self.list_of_dicts
