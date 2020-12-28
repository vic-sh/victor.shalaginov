ip_address_str = input('Enter IP address: ')

ip_adress_first_octet = int(ip_address_str.split('.')[0])

print(ip_adress_first_octet)

if ip_adress_first_octet >= 1 and ip_adress_first_octet <= 223:
 print('unicast')

elif ip_address_str == '255.255.255.255':
 print('local broadcast')

elif ip_adress_first_octet >= 224 and ip_adress_first_octet <= 239:
 print('multicast')

elif ip_address_str == '0.0.0.0':
 print('unassigned')
else:
 print('unused')
