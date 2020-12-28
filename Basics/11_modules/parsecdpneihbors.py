with open('sw1_sh_cdp_neighbors.txt', 'r') as file_sw1_sh_cdp_neighbors:
    file_str = file_sw1_sh_cdp_neighbors.read()

def parse_cdp_neihbors(filename_str):

    router_name = filename_str.split('>')[0]

    info_from_file = filename_str.split('Port ID')[1]

    device_number = 0
    interface_number1 = 1
    interface_number2 = 2
    local_interface_number1 = 8
    local_interface_number2 = 9
    lenght_of_info = 0
    cdp_neighbors_dict = {}

    while lenght_of_info < len(info_from_file):
        device_id = info_from_file.split()[device_number]

        int_id1 = info_from_file.split()[interface_number1]

        int_id2 = info_from_file.split()[interface_number2]

        int_id = int_id1 + int_id2

        local_interface_id1 = info_from_file.split()[local_interface_number1]

        local_interface_id2 = info_from_file.split()[local_interface_number2]

        local_interface_id = local_interface_id1+local_interface_id2

        lenght_of_info = lenght_of_info + int(len(info_from_file)/3)

        device_number += 10
        interface_number1 += 10
        interface_number2 += 10
        local_interface_number1 += 10
        local_interface_number2 += 10

        dict_key = (router_name, int_id)
        dict_value = (device_id, local_interface_id)

        cdp_neighbors_dict[dict_key] = dict_value

    #print(cdp_neighbors_dict)

    return cdp_neighbors_dict

dict = parse_cdp_neihbors(file_str)

print(dict)

