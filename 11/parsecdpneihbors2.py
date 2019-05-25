with open('sh_cdp_n_r3.txt', 'r') as file_sh_cdp_neighbors:
    file_str = file_sh_cdp_neighbors.read()

cdp_neighbors_dict = {}

def parse_cdp_neihbors(filename_str):

    router_name = filename_str.split('>')[0]
    info_from_file = filename_str.split('Port ID')[1]
    info_from_file_list = info_from_file.split()
    lenght_of_last_items = len(info_from_file_list)

    while lenght_of_last_items > 0:

        device_number = info_from_file_list.index('Eth') - 1
        #print(device_number)
        local_interface_number1 = info_from_file_list.index('Eth')
        local_interface_number2 = info_from_file_list.index('Eth') + 1

        device_id = info_from_file_list[device_number]
        #print(device_id)
        local_int_id1 = info_from_file_list[local_interface_number1]
        local_int_id2 = info_from_file_list[local_interface_number2]
        local_int_id = local_int_id1 + local_int_id2
        #print(local_int_id)

        info_from_file_list.remove('Eth')

        remote_int_number1 = info_from_file_list.index('Eth')
        remote_int_number2 = info_from_file_list.index('Eth') + 1

        remote_int_id1 = info_from_file_list[remote_int_number1]
        remote_int_id2 = info_from_file_list[remote_int_number2]

        remote_int_id = remote_int_id1+remote_int_id2
        #print(remote_int_id)

        info_from_file_list.remove('Eth')

        dict_key = (router_name, local_int_id)
        dict_value = (device_id, remote_int_id)

        cdp_neighbors_dict[dict_key] = dict_value
        #print(cdp_neighbors_dict)
        lenght_of_last_items = len(info_from_file_list) - remote_int_number2
        #print(lenght_of_last_items)

    return cdp_neighbors_dict

if __name__=='__main__':
    dict = parse_cdp_neihbors(file_str)
    print(dict)

