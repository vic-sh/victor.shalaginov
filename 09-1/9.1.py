access_config = []

def generate_access_config(access):

    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    for interface in access_dict.keys():
        vlan = access_dict.get(interface)

        print(interface)
        access_config.append(interface)

        for string in access_template:
            if string.endswith('access vlan'):
                print(' ' + string + ' ' + str(vlan))
                access_config.append(' ' + string + ' ' + str(vlan))
            else:
                print(' ' + string)
                access_config.append(' ' + string)

    return access_config


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

generate_access_config(access_dict)

print(access_config)