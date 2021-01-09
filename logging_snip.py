
import os

currentDirectory = os.path.dirname(os.path.realpath(__file__))

# CHECK: log file can be created
LOG_FILENAME = os.path.join(currentDirectory, "{}.log".format(os.path.basename(__file__)))
logFileDir   = os.path.dirname(LOG_FILENAME)
if not os.path.exists(logFileDir):
  raise FileNotFoundError("log directory does not exist: {}".format(logFileDir))

# create a file logger that automatically rotates log files
import logging
logging.getLogger("").setLevel(logging.DEBUG)
from logging.handlers import RotatingFileHandler
fileHandler = RotatingFileHandler(filename=LOG_FILENAME, maxBytes=5000000, backupCount=5, encoding="utf-8")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger("").addHandler(fileHandler)

# create a console logger
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(message)s"))
logging.getLogger("").addHandler(console)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
  logger.debug("debug honk")
  logger.info("info honk")
  logger.error("error honk")