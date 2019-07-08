import argparse, re
from pprint import pprint
from task15_4 import parse_cfg

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
parser.add_argument('headers', action="store", default='' help="Enter a regex to parse in the file")

args = parser.parse_args()
#print(args)

regex = ('(\S+) +'
         '([\d.]+|\S+)+ +'
         '\w+ +\w+ +'
         '(up|down|administratively down) +'
         '(up|down)')

result2 = parse_cfg(args.filename)
pprint(result2)

