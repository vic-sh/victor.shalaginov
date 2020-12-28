import argparse, re

parser = argparse.ArgumentParser(description='Fileparser with a regex')

parser.add_argument('filename', action="store", help="Enter a name of file to parse")
parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)
'''
fileContent = open(args.filename).read()

stringsListFromTheFile = re.findall('.*'+args.regex+'.*', fileContent)

for string in stringsListFromTheFile:
    print(string)
'''

def return_match(filename, regex):
    substring_list = []
    with open(filename) as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                substring_list.append(match.group(1))
    print(substring_list)

return_match(args.filename, args.regex)

