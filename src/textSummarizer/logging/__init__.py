import os
import sys
import logging
from datetime import datetime


logger_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath=os.path.join(log_dir, LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

"""
    filename: It specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler (Simply giving name to the logger file)
    filemode: If filename is specified, open the file in this mode. Defaults to 'a'. We can write 'w'.
    level: Set the root logger level to the specified level. There are 5 built-in levels i.e., INFO, ERROR, CRITICAL
    format: Use the specified format string for the handler.
    datefmt: Use the specified date/time format, as accepted by time.strftime()
    style: If format is specified, use this style for the format string. One of '%', '{' or '$' for printf-style, str.format() or string.Template respectively. Defaults to '%'.
"""
logging.basicConfig(
    level=logging.INFO,
    format=logger_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
    ]
)

logger=logging.getLogger("textSummarizerLogger")