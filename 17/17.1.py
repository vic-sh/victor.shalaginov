import argparse, re, glob

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

output = ''

regex = ('Cisco IOS Software, \w+  , Version (\S+)'
         'router uptime is (\w+)'
         'System image file is "(\w+)"')

filename = "sh_version_r1.txt"

with open(filename) as f:
    output = f.read()
    print(output)

def parse_sh_version(output):

    pass