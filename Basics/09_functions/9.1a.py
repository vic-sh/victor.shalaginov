access_config = []

def generate_access_config(access, psecurity = False):

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

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
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
            if psecurity:
                for string in port_security:
                    print(' ' + string)
                    access_config.append(' ' + string)

    return access_config


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

generate_access_config(access_dict, psecurity = True)

print(access_config)