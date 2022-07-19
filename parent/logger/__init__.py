import logging
from datetime import datetime
import os
from parent.constants import get_current_time_stamp

########################################################################################################################################
# Function that will create a log files with timestamp value
def create_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = create_log_file_name()


########################################################################################################################################
# Create LOG FILE DIRECTORY
LOG_DIR = "logs"

# os.makedirs will create a new folder called "logs" in the current working directory if the folder doesnt already exist
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s];%(levelname)s;%(lineno)d;%(filename)s;%(funcName)s();%(message)s',
level=logging.INFO
)