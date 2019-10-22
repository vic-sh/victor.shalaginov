interface_mode = input('Enter interface mode (access/trunk): ')
interface_type_and_number = input('Enter interface type and number: ')

mode_question = {'access': 'Enter VLAN number: ', 'trunk': 'Enter allowed VLANs: '}

vlans = input(mode_question.get(interface_mode))
print('')
print('interface', interface_type_and_number)

#print(type(interface_mode + '_template'))

#print(list_name[0])

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

interface_mode_dict = {'access': access_template, 'trunk': trunk_template}

print('\n'.join(interface_mode_dict.get(interface_mode)).format(vlans))
#print(interface_mode_dict.get(interface_mode))
