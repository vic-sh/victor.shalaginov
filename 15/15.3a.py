import argparse, re

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
#parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

regex = ('interface (?P<intf>\S+)'
         '|ip address (?P<ip>\S+) (?P<mask>\S+)')

def parse_cfg(filename):

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match.lastgroup == 'intf':
                interface = match.group(match.lastgroup)
            elif interface:
                tuple = (match.group(2), match.group(3))
                result[interface] = tuple

        print(result)

    return result

'''
    for element in match:
        if element[0] != '':
            print(element)
            
            
'''

result2 = parse_cfg(args.filename)


print(result2)

