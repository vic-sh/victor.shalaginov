ignore = ['duplex', 'alias', 'Current configuration']
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
        for line in file:

            if ignore_command(line, ignore):
                if not line.startswith('!'):

                    if not line.startswith(' '):
                        dict_key = line.strip('\n')
                        dict_value = []

                    else:
                        dict_value.append(line.strip('\n'))

                config_dict[dict_key] = dict_value
    print(config_dict)


    return

cfg_check('config_sw1.txt')

