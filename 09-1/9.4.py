config_dict = {}
def get_int_vlan_map(filename):
    access_vlan = {'FastEthernet0/12': 10,
                    'FastEthernet0/14': 11,
                    'FastEthernet0/16': 17}
    trunk_vlan = {'FastEthernet0/1':[10,20],
                  'FastEthernet0/2':[11,30],
                  'FastEthernet0/4':[17]}
    with open(filename, 'r') as file:
        for line in file:

            if line.startswith('interface'):
                #print(line.split()[1])
                interface = line.split()[1]

            if line.endswith('mode access\n'):
                vlan = 1
                config_dict[interface] = int(vlan)

            if line.startswith(' switchport access'):
                vlan = line.split()[3]
                config_dict[interface] = int(vlan)

            if line.startswith(' switchport trunk allowed'):
                #print(line.split()[4])
                vlan_str = line.split()[4]
                vlan_list = vlan_str.split(',')
                vlan_list_int = []
                for vlan in vlan_list:
                    vlan_int = int(vlan)
                    #print(vlan_int)
                    vlan_list_int.append(vlan_int)
                config_dict[interface] = vlan_list_int

get_int_vlan_map('config_sw2.txt')
print(config_dict)
