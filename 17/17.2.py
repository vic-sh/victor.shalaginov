import re

filename = "sh_cdp_n_sw1.txt"
dictionary = {}
dictionary_string = {}
dictionary_list = {}

regex = ('(\S+) + (Eth \d/\d) + (?:\d+) +R S I +(?:\w+) +(Eth \d/\d)')

with open(filename) as f:
    output_from_the_file = f.read()

#print(output_from_the_file)
hostname = output_from_the_file.split('>')[0]

def parse_sh_cdp_neighbors(output_from_the_file_arg):
    match_iter = re.finditer(regex, output_from_the_file_arg)
    return match_iter

result = parse_sh_cdp_neighbors(output_from_the_file)
#print(result.groups())

for match in result:

    dictionary_string = {match.group(1): match.group(3)}
    dictionary_list[match.group(2)] = dictionary_string
    dictionary_string = {}

    dictionary = {hostname: dictionary_list}
print(dictionary)




'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

