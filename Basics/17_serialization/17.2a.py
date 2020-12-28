import glob,pprint,yaml
import re
from task17_2 import parse_sh_cdp_neighbors

#sh_cdp_n_files = ["sh_cdp_n_r5.txt"]
sh_cdp_n_files = glob.glob('sh_cdp_n*')
print(sh_cdp_n_files)

topology = {}
dictionary = {}
dictionary_fin = {}
dictionary_string = {}
dictionary_list = {}

regex = ('(\S+) +(Eth \d/\d) + (?:\d+) +(?:\w )+ +(?:\S+) +(Eth \d/\d)')
#regex = ('(\S+) +(Eth \d/\d) + \d+ +S I +(?:\w+) +(Eth \d/\d)')

#def parse_sh_cdp_neighbors(output_from_the_file_arg):
#    match_iter = re.finditer(regex, output_from_the_file_arg)
#    return match_iter

for filename in sh_cdp_n_files:
    with open(filename) as f:
        output_from_the_file = f.read()

    #print(output_from_the_file)
    hostname = output_from_the_file.split('>')[0]

    #regex = ('(\S+) +(Eth \d/\d) + (?:\d+) +(?:\w )+ +(?:\S+) +(Eth \d/\d)')

    result = parse_sh_cdp_neighbors(output_from_the_file)
    #print(result.groups())

    for match in result:
        #print(match.group())
        #print(match.group(1))
        #print(match.group(2))
        #print(match.group(3))

        dictionary_string = {match.group(1): match.group(3)}
        dictionary_list[match.group(2)] = dictionary_string
        dictionary_string = {}

    dictionary = {hostname: dictionary_list}
    dictionary_list = {}
    dictionary_fin.update(dictionary)
    dictionary = {}

pprint.pprint(dictionary_fin)

topology = dictionary_fin

with open('topology.yaml', 'w') as f:
    yaml.dump(topology, f)


'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''
