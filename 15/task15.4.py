import argparse, re
from pprint import pprint

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
#parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

regex = ('(\S+) +'
         '([\d.]|\S+)+ +'
         '\w+ +\w+ +'
         '(up|down|administratively down) +'
         '(up|down)')

def parse_cfg(filename):

    result = []

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            result.append(match.groups())

    return result

result2 = parse_cfg(args.filename)
pprint(result2)

