import pprint

ignore = ['duplex', 'alias', 'Current configuration']
dict_key = ''
config_dict = {}
config_dict2 = {}
dict_value = []
dict_value2 = []

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def cfg_check(filename):

    with open(filename, 'r') as file:

        #dict_value = []
        #dict_key = ''

        for line in file:

            if ignore_command(line, ignore):
                continue

            if not "!" in line:


                if not line.startswith('  ') and not line.startswith(' '):

                    dict_key = line.strip('\n')
                    dict_value = []
                    dict_value2 = []

                elif not line.startswith('  '):

                    dict_value.append(line.strip('\n'))
                    dict_value2 = []
                    dict_value_str = line.strip('\n')

                else:

                    dict_value2.append(line.strip('\n'))


                if dict_value2 == []:

                    config_dict[dict_key] = dict_value

                else:

                    config_dict2[dict_value_str] = dict_value2
                    config_dict[dict_key] = config_dict2

    return config_dict

cfg_check('config_r1.txt')

print(config_dict)
pprint.pprint(config_dict)

