import argparse, re
from pprint import pprint

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
#parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

regex = ('interface (?P<intf>\S+)'
         '|ip address (?P<ip_sec>\S+) (?P<mask_sec>\S+) secondary'
         '|ip address (?P<ip>\S+) (?P<mask>\S+)\s')

def parse_cfg(filename):

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:

            if match.lastgroup == 'intf':
                interface = match.group(match.lastgroup)

            elif match.lastgroup == 'mask':
                tuple = (match.group(4), match.group(5))
                list_of_tuple = [tuple]
                result[interface] = list_of_tuple

            elif match.lastgroup == 'mask_sec':
                tuple_sec = (match.group(2), match.group(3))
                list_of_tuple.append(tuple_sec)
                result[interface] = list_of_tuple

    return result

result2 = parse_cfg(args.filename)
pprint(result2)

