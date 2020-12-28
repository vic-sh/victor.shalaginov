

ip_address_correct = False

while not ip_address_correct:

    ip_address_str = input('Enter IP address: ')
    ip_address_list = ip_address_str.split('.')

    if len(ip_address_list) == 4 and int(ip_address_str.split('.')[0]) <= 255 and int(ip_address_str.split('.')[1]) <= 255 and int(ip_address_str.split('.')[2]) <= 255 and int(ip_address_str.split('.')[3]) <= 255:

        if int(ip_address_str.split('.')[0]) >= 1 and int(ip_address_str.split('.')[0]) <= 223:
            print('unicast')
        elif ip_address_str == '255.255.255.255':
            print('local broadcast')
        elif int(ip_address_str.split('.')[0]) >= 224 and int(ip_address_str.split('.')[0]) <= 239:
            print('multicast')
        elif ip_address_str == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
        ip_address_correct = True
        continue

    else:
        print('Incorrect IPv4 address')

