import netifaces
# import pcapy
import psutil, sys
from time import sleep
from scapy.all import *

def main_menu():
    print("Please choose the menu you want to start:")
    print("1. Multicast Dest LAN->WAN")
    print("2. Multicast Src WAN->LAN")
    print("3. ExtHdrRouting to the packet WAN->LAN")
    print("4. Set MAC and IPs")
    #print("5. Clear")
    print("0. Quit")
    choice = input(">>Select>> ")
    exec_menu(choice)

def exec_menu(choice):
    if choice == '1':
        McastDestLANWAN()
    elif choice == '2':
        McastSrcWANLAN()
    elif choice == '3':
        ExtRoutWANLAN()
    elif choice == '4':
        change_ip_mac()
    else:
        sys.exit()

def McastDestLANWAN():
    #print("1")
    base = IPv6()
    base.dst = 'ff01:0:0:0:0:0:0:fc'  # Multicast address in IPv6
    base.src = IPv6_en0_ip
    prot = UDP(sport=5001, dport=5001)  # Attributes can be defined in initialization
    data = Raw(load="Important message to Irina!")
    packet = base / prot / data  # '/' encapsulates the messages
    packet.show()  # Displays the fields in the packet
    print("Sending packets from", base.src, "to", base.dst, " LAN->WAN")
    send(packet, count=5000)
    print("Sleeping 3 sec...")
    sleep(3)
    main_menu()

def McastSrcWANLAN():
    # Construct packets with multicast Src WAN->LAN
    base = IPv6()
    base.dst = IPv6_base_dst  #
    base.src = 'ff01:0:0:0:0:0:0:fc'  # Multicast address in IPv6
    prot = UDP(sport=5001, dport=5001)  # Attributes can be defined in initialization
    data = Raw(load="Important message to Irina!")
    packet = Ether(dst=Ether_dst) / base / prot / data
    packet.show()  # Displays the fields in the packet
    print("Sending packets from", base.src, "to", base.dst, " WAN->LAN")
    print("Sleeping 3 sec...")
    sleep(3)
    sendp(packet, count=5000)
    # for NN in range(1):
    #    sendp(packet)
    print("Sleeping 3 sec...")
    sleep(3)
    main_menu()

def ExtRoutWANLAN():
    # Adding ExtHdrRouting to the packet WAN->LAN
    base = IPv6()
    ext = IPv6ExtHdrRouting(addresses=[IPv6ExtHdrRouting_addresses])
    base.src = IPv6_en0_ip
    print("Sending packets from", base.src, "to", base.dst, "with EH", IPv6ExtHdrRouting_addresses, " WAN->LAN")
    prot = UDP(sport=5001, dport=5001)  # Attributes can be defined in initialization
    data = Raw(load="Important message to Irina!")
    packet = Ether(dst=Ether_dst) / base / ext / prot / data
    packet.show()  # Displays the fields in the packet
    sendp(packet, count=5000)
    print("Sleeping 3 sec...")
    sleep(3)
    main_menu()
    # for NN in range(1):
    #    sendp(packet)

def change_ip_mac():
    global Ether_dst, IPv6_base_dst, IPv6ExtHdrRouting_addresses
    Ether_dst = input('Enter CPE Ethernet MAC WAN address 74:9D:79:89:32:5C   ')
    IPv6_base_dst = input('Enter CPE IPv6 WAN address 2a01:620:2:1d00:2e41:38ff:fe98:5014   ')
    IPv6ExtHdrRouting_addresses = input('Enter PC behind CPE IPv6 address for ExtHdrRouting 2a01:620:2:1d00:f8b8:1bb4:2d21:88f6   ')
    main_menu()

if __name__ == '__main__':
    # Find IPv6 source address of the interface
    all_ips_and_ifaces = psutil.net_if_addrs()  # Read all IPs and the list of all ifaces
    # print(all_ips_and_ifaces)
    en0_ips_and_ifaces = all_ips_and_ifaces['enp0s25']  # !!!_Change_if_necessary_Read all IPs and the other params from enX
    print("+" * 20)
    IPv6_en0_ips_and_ifaces = en0_ips_and_ifaces.pop(1)  # class with string of the IPv6 address
    # !!!!_Change_before_use!!!!!!! Addresses of the CPE and PC behind it
    Ether_dst = "74:9D:79:89:32:5C"  # CPE Ethernet WAN address
    IPv6_base_dst = '2a01:620:2:f20::60'  # CPE IPv6 WAN address 2a01:620:2:1d00:2e41:38ff:fe98:5014
    IPv6ExtHdrRouting_addresses = "2a01:620:2:c:90ce:a1b:90d5:fe4b"  # PC behind CPE IPv6 address for ExtHdrRouting 2a01:620:2:1d00:f8b8:1bb4:2d21:88f6
    print("CPE Ethernet WAN address", Ether_dst)
    print("CPE IPv6 WAN address", IPv6_base_dst)
    print("PC behind CPE IPv6 address for ExtHdrRouting", IPv6ExtHdrRouting_addresses)
    # print('IPv6_en0_ips_and_ifaces')
    IPv6_en0_ip = IPv6_en0_ips_and_ifaces.address
    print("enX IPv6 address is", IPv6_en0_ip)
    print("+" * 20)
    main_menu()


'''
# Construct packets with multicast Dest LAN->WAN
base = IPv6()
base.dst = 'ff01:0:0:0:0:0:0:fc'  # Multicast address in IPv6
base.src = IPv6_en0_ip
prot = UDP(sport=5001, dport=5001)  # Attributes can be defined in initialization
data = Raw(load="Important message to Irina!")
packet = base / prot / data  # '/' encapsulates the messages

packet.show()  # Displays the fields in the packet

print("Sending packets from", base.src, "to", base.dst, " LAN->WAN")

send(packet, count=5000)
# for NN in range(3000):
#    send(packet)

print("Sleeping 3 sec...")
sleep(3)

# Construct packets with multicast Src WAN->LAN
base.dst = IPv6_base_dst  #
base.src = 'ff01:0:0:0:0:0:0:fc'  # Multicast address in IPv6
packet = Ether(dst=Ether_dst) / base / prot / data
print("Sending packets from", base.src, "to", base.dst, " WAN->LAN")

sendp(packet, count=5000)
# for NN in range(1):
#    sendp(packet)

print("Sleeping 3 sec...")
sleep(3)

# Adding ExtHdrRouting to the packet WAN->LAN
ext = IPv6ExtHdrRouting(addresses=[IPv6ExtHdrRouting_addresses])
base.src = IPv6_en0_ip
print("Sending packets from", base.src, "to", base.dst, "with EH", IPv6ExtHdrRouting_addresses, " WAN->LAN")
packet = Ether(dst=Ether_dst) / base / ext / prot / data
packet.show()  # Displays the fields in the packet

sendp(packet, count=5000)
# for NN in range(1):
#    sendp(packet)
'''
