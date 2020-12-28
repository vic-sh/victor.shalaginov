trunk_config_list = []

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for interface in trunk_dict.keys():
        trunk_config_list.append(interface)
        for string in trunk_template:
            if string.endswith('allowed vlan'):
                print(trunk_dict.get(interface))
                trunk_list_with_brackets = trunk_dict.get(interface)
                print(str(trunk_list_with_brackets)[1:(len(str(trunk_list_with_brackets))-1)])
                trunk_config_list.append(string + ' ' + str(trunk_list_with_brackets)[1:(len(str(trunk_list_with_brackets))-1)])
            else:
                trunk_config_list.append(string)

trunk_dict = { 'FastEthernet0/1' :[10 ,20 ,30],
               'FastEthernet0/2' :[11 ,30],
               'FastEthernet0/4' :[17] }

generate_trunk_config(trunk_dict)
print(trunk_config_list)