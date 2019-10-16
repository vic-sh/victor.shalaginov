# -*- coding: utf-8 -*-

import glob,pprint,yaml
from task17_2 import parse_sh_cdp_neighbors

sh_cdp_n_files = glob.glob('sh_cdp_n*')
#print(sh_cdp_n_files)

#topology = {}
#dictionary = {}
#dictionary_fin = {}
#dictionary_string = {}
#dictionary_list = {}
#regex = ('(\S+) +(Eth \d/\d) + (?:\d+) +(?:\w )+ +(?:\S+) +(Eth \d/\d)')

def generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology2.yaml'):
    topology = {}
    dictionary = {}
    dictionary_fin = {}
    dictionary_string = {}
    dictionary_list = {}
    regex = ('(\S+) +(Eth \d/\d) + (?:\d+) +(?:\w )+ +(?:\S+) +(Eth \d/\d)')

    for filename in list_of_files:
        with open(filename) as f:
            output_from_the_file = f.read()

        hostname = output_from_the_file.split('>')[0]
        result = parse_sh_cdp_neighbors(output_from_the_file)

        for match in result:

            dictionary_string = {match.group(1): match.group(3)}
            dictionary_list[match.group(2)] = dictionary_string
            dictionary_string = {}

        dictionary = {hostname: dictionary_list}
        dictionary_list = {}
        dictionary_fin.update(dictionary)
        dictionary = {}

    pprint.pprint(dictionary_fin)
    topology = dictionary_fin
    if save_to_file:
        with open(topology_filename, 'w') as f:
            yaml.dump(topology, f)
    return topology

topology_fin = generate_topology_from_cdp(sh_cdp_n_files)

pprint.pprint(topology_fin)

'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''