from reader.reader_integrator import ReaderIntegrator, create_timestamp
from logger.tools import Logger
import config
import os
import writer.xls_writer as wr

log = Logger()


@create_timestamp
def save_to_xls(local_reader_data):
    data = wr.XLSGen(local_reader_data)
    destination = config.output_dirs
    data.to_xls(destination)


@create_timestamp
def input_folder_check():
    input_folder = config.input_dir
    if not os.path.isdir(input_folder):
        log.general.warning(f"Input path do not exists - creating destination {input_folder}")
        os.mkdir(input_folder)


if __name__ == '__main__':
    try:
        log.business.info(f"Bot Started")
        failed_files = []
        input_folder_check()
        reader = ReaderIntegrator(config.input_dir)
        reader.recognized_file_structure()
        reader.recognized_file_names()
        reader_data = reader.extractor()
        save_to_xls(reader_data)
        log.business.info(f"Bot Finished")

    except Exception as err:
        log.general.info(f"Terminating the bot. Exception: {err}")
        status = f"Error while processing the mail. Error description: {err}"
