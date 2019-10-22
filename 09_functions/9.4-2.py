ignore = ['duplex', 'alias', 'Current configuration']
dict_key = ''
config_dict = {}
dict_value = []

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

        dict_value = []
        dict_key = ''

        for line in file:

            if not line.startswith('!'):

                if not line.startswith(' '):
                    if ignore_command(line, ignore):
                        continue

                    else:
                        dict_key = line.strip('\n')
                        dict_value = []

                else:
                    if ignore_command(line, ignore):
                        continue
                    else:
                        dict_value.append(line.strip('\n'))

            config_dict[dict_key] = dict_value

    return config_dict

cfg_check('config_sw1.txt')

print(config_dict)

