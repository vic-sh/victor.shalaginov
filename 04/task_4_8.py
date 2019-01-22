IP = '192.168.3.1'

IP_LIST = IP.split('.')

template = ''' 
{0:<10} {1:<10} {2:<10} {3:<10} 
{4:<010b} {5:<010b} {6:<010b} {7:<010b} 
'''

print(template.format(IP_LIST[0],IP_LIST[1],IP_LIST[2],IP_LIST[3],int(IP_LIST[0]),int(IP_LIST[1]),int(IP_LIST[2]),int(IP_LIST[3])))
