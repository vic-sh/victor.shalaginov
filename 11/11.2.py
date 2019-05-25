from  parsecdpneihbors import parse_cdp_neihbors
from draw_network_graph import draw_topology

with open('sw1_sh_cdp_neighbors.txt', 'r') as file_sw1_sh_cdp_neighbors:
    file_str = file_sw1_sh_cdp_neighbors.read()

parsed_cdp_dict = parse_cdp_neihbors(file_str)

draw_topology(parsed_cdp_dict)









