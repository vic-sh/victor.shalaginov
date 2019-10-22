from  parsecdpneihbors2 import parse_cdp_neihbors
from draw_network_graph import draw_topology

list_of_files = ['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_sw1.txt']
parsed_cdp_dict = {}
sum_of_parsed_cdp_dict = {}

for file in list_of_files:
    with open(file, 'r') as file_sh_cdp_neighbors:

        file_str = file_sh_cdp_neighbors.read()
        parsed_cdp_dict = parse_cdp_neihbors(file_str)
        sum_of_parsed_cdp_dict.update(parsed_cdp_dict)

for key in sum_of_parsed_cdp_dict.copy().keys():
    for value in sum_of_parsed_cdp_dict.copy().values():
        if key == value:
            print(key, value)
            del(sum_of_parsed_cdp_dict[key])


print(sum_of_parsed_cdp_dict)

draw_topology(sum_of_parsed_cdp_dict)









