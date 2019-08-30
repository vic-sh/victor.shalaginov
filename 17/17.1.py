import argparse, re, glob

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

output = ''

#regex = ('.+\), Version (\S+),.+'
#         'router uptime is (\S+ days, \S+ hours, \S+ minutes).+'
#         'System image file is "(\S+)"')

filename = "sh_version_r1.txt"

with open(filename) as f:
    output_from_the_file = f.read()

def parse_sh_version(output):
    result = []
    match_iter = re.search(regex, output)

#    for match in match_iter:
#        result.append(match.groups())
#    return result

result = parse_sh_version(output_from_the_file)
print(result)

