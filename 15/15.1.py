import argparse, re

parser = argparse.ArgumentParser(description='Fileparser with a regex')

parser.add_argument('filename', action="store", help="Enter a name of file to parse")
parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

fileContent = open(args.filename).read()

stringsListFromTheFile = re.findall('.+'+args.regex+'.+', fileContent)

for string in stringsListFromTheFile:
    print(string)


