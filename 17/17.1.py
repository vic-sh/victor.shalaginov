import argparse, re, glob, csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']
list_of_values = []
list_of_lists = []
output = ''
match = ''
output_from_the_file_stripped = ''

regex = ('.+\), Version (\S+), (?:.+\s){7}'
         'router uptime is (\S+ days, \S+ hours, \S+ minutes)\s.+\s'
         'System image file is "(.+)"\s')

filename = "sh_version_r1.txt"

def parse_sh_version(output):
    match = re.search(regex, output)
    return match

def write_to_csv(filename, list_of_lists):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for row in list_of_lists:
            writer.writerow(row)
    with open(filename, 'r') as f:
        print(f.read())

list_of_values.extend(headers)
print(list_of_values)
list_of_lists.append(list_of_values)
print(list_of_lists)

for filename in sh_version_files:
    hostname = filename[11:13]
    with open(filename) as f:
        output_from_the_file = f.read()
        output_from_the_file_stripped = output_from_the_file.strip()
    result = parse_sh_version(output_from_the_file_stripped)
    print(list(result.groups()))
    list_of_lists.append(list(result.groups()))

print(list_of_lists)
write_to_csv('file_with.csv', list_of_lists)
    #list =
    #list.extend(list(match))
    #print(list)




