template = ''' 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: {:<25}{:<25} 
    ...: '''  

print(template.format('Protocol:', 'OSPF', 'Prefix:', ospf_route.split()[1], 'AD/Metric:',ospf_route.split()[2][1:7], 'Next-Hop:', ospf_route.split()[4], 'Last update:', ospf_route.split()[5], 'Outbound Interface:', ospf_route.split()[6]))                                                                                           

Protocol:                OSPF                     
Prefix:                  10.0.24.0/24             
AD/Metric:               110/41                   
Next-Hop:                10.0.13.3,               
Last update:             3d18h,                   
Outbound Interface:      FastEthernet0/0
