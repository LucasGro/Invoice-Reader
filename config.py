from datetime import datetime
import codecs
import os
import json

try:
    with codecs.open('config.json', 'r', 'utf-8-sig') as json_file:
        config_data = json.load(json_file)

    BASE_DIR = os.getcwd()
    start_time = datetime.now()
    input_dir = config_data['Folder']['Input']
    output_dirs = config_data['xls']['destination']['Output']
    status = "OK"

except Exception as err:
    status = f"Failed, error details: {err}"
