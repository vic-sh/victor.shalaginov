import argparse, re
from pprint import pprint
from task15_4 import parse_cfg

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
parser.add_argument('-l', action="store", dest='headers', default=['interface', 'address', 'status', 'protocol'], help="Enter a regex to parse in the file", type=list)

args = parser.parse_args()
#print(args)

regex = ('(\S+) +'
         '([\w.]+)+ +'
         '\w+ +\w+ +'
         '(up|down|administratively down) +'
         '(up|down)')

result2 = parse_cfg(args.filename)
#pprint(result2)
#print(args.headers)

listOfDict = []
dictionary = {}

def convert_to_dict(result3):
    for match in result3:
        #print(list(match))
        #print(dict(zip(args.headers,list(match))))
        dictionary = dict(zip(args.headers,list(match)))
        listOfDict.append(dictionary)
    return listOfDict

convert_to_dict(result2)
print(listOfDict)
