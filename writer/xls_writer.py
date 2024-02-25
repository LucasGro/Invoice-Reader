import pandas as pd
import logger.tools as lg
import os

log = lg.Logger()


class XLSGen:
    """Genertes XLS files that contains data from PDF file"""

    def __init__(self, ticket_info):
        self.__ticket = ticket_info
        self.reader_data = []
        self.__ticket = [{x: str(y) for x, y in t.items()} for t in self.__ticket]
        self.__type = None

    def to_xls(self, dst):
        if not os.path.isdir(os.path.dirname(dst)):
            log.general.warning(f'Destination path do not exists. Creating destination{os.path.dirname(dst)}...')
            os.mkdir(os.path.dirname(dst))

        try:
            log.general.info(f'Creating new xls file in path: {dst}')
            df = pd.DataFrame(self.__ticket)
            df.to_excel(dst, index=False)
            lines = len(df)
            log.general.info(f'Success. Number of lines written: {lines}')
            log.business.info(f'Success. Number of items processed: {lines}')
        except Exception as err:
            log.general.error(err)
            raise Exception(err)

        return
