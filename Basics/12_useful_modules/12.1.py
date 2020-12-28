import subprocess,argparse

available_ip_list = []
not_available_ip_list = []

def check_ip_addresses(ip_addresses_list):

    for ip_address in ip_addresses_list:

        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address], stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            available_ip_list.append(ip_address)

        else:
            not_available_ip_list.append(ip_address)

    return available_ip_list, not_available_ip_list

parser = argparse.ArgumentParser(description='Ping a list of addresses')
parser.add_argument('-l', action="store", dest="ip_list", default='8.8.8.8')
args=parser.parse_args()
print(args)

check_ip_addresses(args.ip_list.split(','))

print(available_ip_list)
print(not_available_ip_list)