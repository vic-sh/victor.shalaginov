import netifaces
import pcapy
import psutil
from time import sleep
from scapy.all import *

#Find IPv6 source address of the interface
all_ips_and_ifaces = psutil.net_if_addrs() # Read all IPs and the list of all ifaces
print(all_ips_and_ifaces)
en0_ips_and_ifaces = all_ips_and_ifaces['en3'] # !!!_Change_if_necessary_Read all IPs and the other params from enX
print("+++")
IPv6_en0_ips_and_ifaces = en0_ips_and_ifaces.pop(3) # class with string of the IPv6 address

#!!!!_Change_before_use!!!!!!! Addresses of the CPE and PC behind it
Ether_dst = "EC:4C:4D:33:67:42" #CPE Ethernet WAN address
IPv6_base_dst = '2a01:620:2:f20::48' # CPE IPv6 WAN address 2a01:620:2:1d00:2e41:38ff:fe98:5014
IPv6ExtHdrRouting_addresses = "2a01:620:2:f20::3e" # PC behind CPE IPv6 address for ExtHdrRouting 2a01:620:2:1d00:f8b8:1bb4:2d21:88f6
print("CPE Ethernet WAN address", Ether_dst)
print("CPE IPv6 WAN address", IPv6_base_dst)
print("PC behind CPE IPv6 address for ExtHdrRouting", IPv6ExtHdrRouting_addresses)

#print('IPv6_en0_ips_and_ifaces')
      
IPv6_en0_ip = IPv6_en0_ips_and_ifaces.address
print("enX IPv6 address is", IPv6_en0_ip)
print("+++")

#Construct packets with multicast Dest
base = IPv6() 
base.dst = 'ff01:0:0:0:0:0:0:fc' # Multicast address in IPv6
base.src = IPv6_en0_ip 
prot = UDP(sport=5001, dport=5001) # Attributes can be defined in initialization
data = Raw(load="Important message to Irina!")
packet = base / prot / data # '/' encapsulates the messages
 
packet.show() # Displays the fields in the packet

print("Sending packets from", base.src, "to", base.dst)

send(packet, count=10000)
#for NN in range(3000):
#    send(packet)
    
print("Sleeping 3 sec...")
sleep(3)

# Construct packets with multicast Src
base.dst = IPv6_base_dst # 
base.src = 'ff01:0:0:0:0:0:0:fc' # Multicast address in IPv6
packet = Ether(dst=Ether_dst) / base / prot / data
print("Sending packets from", base.src, "to", base.dst)

sendp(packet, count=10000)
#for NN in range(1):
#    sendp(packet)

print("Sleeping 3 sec...")
sleep(3)

#Adding ExtHdrRouting to the packet
ext = IPv6ExtHdrRouting(addresses=[IPv6ExtHdrRouting_addresses])
base.src = IPv6_en0_ip
print("Sending packets from", base.src, "to", base.dst, "with EH", IPv6ExtHdrRouting_addresses)
packet = Ether(dst=Ether_dst) / base / ext / prot / data 
packet.show() # Displays the fields in the packet

sendp(packet, count=10000)
#for NN in range(1):
#    sendp(packet)

