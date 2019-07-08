import argparse, re
from pprint import pprint

parser = argparse.ArgumentParser(description='Fileparser IP address + Mask')
parser.add_argument('filename', action="store", help="Enter a name of file to parse")
#parser.add_argument('regex', action="store", help="Enter a regex to parse in the file")

args = parser.parse_args()
print(args)

regex = ('Group: (\S+) +')

def parse_cfg(filename):

    result = []
    number = 1

    with open(filename) as f:

        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            string1 = '\n#EXTINF:0,0' + str(number)
            number += 1
            #print(string1)
            result.append(string1)
            result_strip1 = str(match.groups()).strip('[(|)|\'|\'|,]')
            string2 = '\nudp://@' + result_strip1 + ':5000'
            #print(string2)
            result.append(string2)

    return result

result2 = parse_cfg(args.filename)
print(result2)

file2 = open('405_2.m3u', 'w')
file2.writelines(result2)
file2.close()



