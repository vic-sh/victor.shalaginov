london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device_name = input('Enter device name (r1,r2 or sw1) ')
parameter_name_cut = str(london_co[device_name].keys()).replace('dict_keys([','').replace('])','').replace("'","")

#print(london_co.get(device_name))
#print('Enter parameter name (', str(london_co[device_name].keys()),')')
print("Enter parameter name (",parameter_name_cut,")")
parameter_name = input()
#parameter_name = input('Enter parameter name (',london_co[device_name].keys(),') ' )
print(london_co[device_name].get(parameter_name, 'oppss!'))
