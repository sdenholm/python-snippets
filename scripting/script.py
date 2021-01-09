import argparse
import logging
import sys
import os
import platform
import subprocess

# default logging level is debug
logging.getLogger("").setLevel(logging.DEBUG)

# directory this file is in
currentDirectory = os.path.dirname(os.path.realpath(__file__))

#############################################################################
# Setup arguments
#############################################################################

# parser
parser = argparse.ArgumentParser()

# arguments
parser.add_argument(metavar="operation", type=str, dest="operation",
                    help="operation to carry out")
parser.add_argument(metavar="number", type=int, dest="number",
                    help="a number, an integer, an argument for the ages")

# optional arguments
parser.add_argument("--verbose", action="store_true", help="turn on verbose mode")
parser.set_defaults(verbose=False)


#############################################################################
# Process arguments
#############################################################################

# parse the arguments
args = parser.parse_args()

# Setup console logger
#  -verbose turns on DEBUG messages
console = logging.StreamHandler()
console.setLevel(logging.DEBUG if args.verbose else logging.INFO)
console.setFormatter(logging.Formatter("%(message)s"))
logging.getLogger("").addHandler(console)
logger = logging.getLogger(__name__)



#############################################################################
# Perform operation
#############################################################################

if __name__ == "__main__":

  # windows needs shell
  shell = platform.system().lower() == "windows"
  
  # run echo command
  cmd = ["echo", "operation: {}, number: {}".format(args.operation, args.number)]
  ret = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
  
  # log messages
  logger.info("This is the current directory: {}".format(currentDirectory))
  logger.info("This is the operating system: {}".format(platform.system()))
  
  # print messages
  logger.info("This is what was output to stdout:", ret.stdout.decode("utf-8"))
  logger.info("This is what was output to stderr:", ret.stderr.decode("utf-8"))
  
  sys.exit(0)