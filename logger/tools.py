from datetime import datetime
import logging
import sys
import uuid


DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL
GENERAL_FORMAT = '{levelname} | {asctime} | module: {module}| file: {filename} | line:{lineno} | function: {funcName} | message: {message}'
BUSINESS_FORMAT = '{levelname} | {asctime} | {message}'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ID = datetime.now().strftime('%Y%m%d%H%M%S%f')


class LoggerInitException(Exception):
    def __init__(self):
        super().__init__('General exception connected with Logger initalization')


class Logger:
    def __init__(self, file_output=f'logs {ID}', standard_output=True, business_level=True):
        self.__file = f"{file_output}.log"
        self.__business_file = f"{file_output}_business.log"
        self.__std = bool(standard_output)
        self.__business_level = business_level
        self.__general_formatter = logging.Formatter(GENERAL_FORMAT, DATE_FORMAT, "{")
        self.__business_formatter = logging.Formatter(BUSINESS_FORMAT, DATE_FORMAT, "{")

        self.__id = str(uuid.uuid4())
        self.general = logging.getLogger(self.__id)
        self.general.setLevel(DEBUG)

        if file_output:
            with open(self.__file, "wt") as file:
                header = GENERAL_FORMAT.replace("{", "").replace("}", "")
                file.write(f"{header}\n")
            self.__file_handler = logging.FileHandler(self.__file)
            self.__file_handler.setFormatter(self.__general_formatter)
            self.general.addHandler(self.__file_handler)
        else:
            raise LoggerInitException

        if standard_output:
            self.__std_handler = logging.StreamHandler(sys.stdout)
            self.__std_handler.setLevel(DEBUG)
            self.__std_handler.setFormatter(self.__general_formatter)
            self.general.addHandler(self.__std_handler)

        if business_level:
            with open(self.__business_file, "wt") as file:
                header = BUSINESS_FORMAT.replace("{", "").replace("}", "")
                file.write(f"{header}\n")
            self.business = logging.getLogger(f"{self.__id}-business")
            self.business.setLevel(business_level)
            self.__business_file_handler = logging.FileHandler(self.__business_file)
            self.__business_file_handler.setFormatter(self.__business_formatter)
            self.business.addHandler(self.__business_file_handler)
        else:
            raise LoggerInitException
