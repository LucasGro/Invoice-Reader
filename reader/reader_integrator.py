from logger.tools import Logger
from reader.invoice_reader import InvoiceReader
import config
import os

log = Logger()


def create_timestamp(our_function):
    def inner_wrapper(*args, **kwargs):
        try:
            log.general.info(f"Starting execution of funtion {our_function.__name__}")
            result = our_function(*args, **kwargs)
            log.general.info(f"Finished execution of function {our_function.__name__}")
            return result
        except Exception as err:
            log.general.error(
                f'Error occured while executing function {our_function.__name__}. Error description: {err}')
            raise Exception(err)
    return inner_wrapper


class ReaderIntegrator:
    def __init__(self, input_data):
        try:
            log.general.info("Initialize reader instance")
            self.input_data = input_data
            self.number_files = None
            self.result = []
            self.list_of_dicts = []
            log.general.info("Initialization completed.")
        except Exception as err:
            log.general.error(f"Could not init Reader: {err}")

    @create_timestamp
    def recognized_file_structure(self):
        try:
            self.file_names = [name for name in os.listdir(self.input_data)]
            self.number_files = len(self.file_names)
            if self.number_files > 0:
                log.business.info(f"Bot Located input data")
                log.business.info(f"Files located in input folder are: {self.file_names}.")
                log.general.info(f"Files located in input folder. Amount: {self.number_files}.")
            else:
                log.general.info(
                    f"No input provided. Please provide input file in location: {config.BASE_DIR}\\input")
        except Exception as err:
            log.general.error(f"Could not create Folder structure, Error: {err}")
            raise Exception

    @create_timestamp
    def recognized_file_names(self):
        for file_name in self.file_names:
            name, _ = os.path.splitext(file_name)
            result_dict = {"File Name": name}
            self.result.append(result_dict)
        log.general.info(f"Files located in input folder are: {self.result}.")
        return self.result

    @create_timestamp
    def extractor(self):
        for file_name in self.file_names:
            extract = InvoiceReader(f"{self.input_data}/{file_name}", self.list_of_dicts)
            extract.date_extractor()
            extract.number_extractor()
            extract.name_extractor()
            self.merged_dict = extract.merge_results()
        return self.merged_dict
