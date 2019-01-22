from sys import argv

ip_mask = argv[1:]

print(ip_mask)

ip_mask_str = str(ip_mask)

ip_str_start = ip_mask_str.split('/')[0]
mask_dec_str_end = ip_mask_str.split('/')[1]

ip_str = ip_str_start[2:]
mask_str = mask_dec_str_end[:-2]

print(ip_str)
print(mask_str)

ip_list = ip_str.split('.')

print(ip_list)

print(bin(int(ip_list[0])))
print(ip_list[1])
print(ip_list[2])
print(ip_list[3])
