import argparse, re, glob

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

output = ''
match = ''
output_from_the_file_stripped=''

#regex = ('.+\), Version (\S+),.+'
#         'router uptime is (\S+ days, \S+ hours, \S+ minutes).+'
#         'System image file is "(\S+)"')

regex = ('.+\), Version (\S+),.+'
         'router uptime is (\S+ days, \S+ hours, \S+ minutes)')

#regex = ('.+\), Version (\S+) .+(\s.+)+router uptime is (\S+ days, \S+ hours, \S+ minutes)')

filename = "sh_version_r1.txt"

with open(filename) as f:
    output_from_the_file = f.read()
    output_from_the_file_stripped = output_from_the_file.strip()

def parse_sh_version(output):
    result = []
    match = re.search(regex, output)
    print(match.groups())

#    for match in match_iter:
#        result.append(match.groups())
    return match

result = parse_sh_version(output_from_the_file_stripped)

print(match)

