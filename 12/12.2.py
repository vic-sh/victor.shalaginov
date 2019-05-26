import subprocess, argparse, ipaddress

available_ip_list = []
not_available_ip_list = []

def ping_function(ip_address):

    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address], stdout=subprocess.DEVNULL)
    if reply.returncode == 0:
            available_ip_list.append(ip_address)
    else:
            not_available_ip_list.append(ip_address)
    return available_ip_list, not_available_ip_list

def check_ip_addresses(ip_addresses_list):

    for ip_address in ip_addresses_list:
        if len(ip_address.split('-')) == 2:
            ip_address_first_address = ip_address.split('-')[0]
            ip_address_second_address = ip_address.split('-')[1]
            #print(int(ip_address_second_address))
            if len(ip_address_second_address.split('.')) == 1:
                ip_address_first_address_ipv4 = ipaddress.ip_address(ip_address_first_address)
                ip_addr_count = ip_address_first_address_ipv4
                while ip_addr_count != (ip_address_first_address_ipv4 + (int(ip_address_second_address) + 1) - int(ip_address_first_address.split('.')[3])):
                    ping_function(str(ip_addr_count))
                    ip_addr_count+=1
            else:
                ip_address_first_address_ipv4 = ipaddress.ip_address(ip_address_first_address)
                ip_address_second_address_ipv4 = ipaddress.ip_address(ip_address_second_address)
                ip_addr_count = ip_address_first_address_ipv4
                while ip_addr_count != (ip_address_second_address_ipv4 + 1):
                    ping_function(str(ip_addr_count))
                    ip_addr_count += 1
        else:
            ping_function(ip_address)

parser = argparse.ArgumentParser(description='Ping a list of addresses')
parser.add_argument('-l', action="store", dest="ip_list", default='8.8.8.8')
args=parser.parse_args()
print(args)

check_ip_addresses(args.ip_list.replace(' ', '').split(','))

print(available_ip_list)
print(not_available_ip_list)