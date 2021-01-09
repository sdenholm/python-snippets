import argparse
import sys
import os
import platform
import subprocess

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

#############################################################################
# Perform operation
#############################################################################

if __name__ == "__main__":

  # parse the arguments
  args = parser.parse_args()
  
  # windows needs shell
  shell = platform.system().lower() == "windows"
  
  # run echo command
  cmd = ["echo", "operation: {}, number: {}".format(args.operation, args.number)]
  ret = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
  
  # log messages
  print("This is the current directory: {}".format(currentDirectory))
  print("This is the operating system: {}".format(platform.system()))
  
  # print messages
  print("This is what was output to stdout:", ret.stdout.decode("utf-8"))
  print("This is what was output to stderr:", ret.stderr.decode("utf-8"))
  
  sys.exit(0)