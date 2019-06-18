import argparse, re

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
#parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

regex = '([0-9]+\\.[0-9]+\\.[0-9]+\\.+[0-9]+)\s([0-9]+\\.[0-9]+\\.[0-9]+\\.+[0-9]+)'

def return_match(filename):
    file = open(filename).read()
    match = re.findall(regex, file)

    print(match)

return_match(args.filename)

