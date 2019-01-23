file = open('7.1.txt', 'r')

ospf_route = file.read()

template = ''' 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: '''

print(template.format('Protocol:', 'OSPF', 'Prefix:', ospf_route.split()[1], 'AD/Metric:',ospf_route.split()[2][1:7], 'Next-Hop:', ospf_route.split()[4], 'Last update:', ospf_route.split()[5], 'Outbound Interface:', ospf_route.split()[6]))