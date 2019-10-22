
file_list = []

with open('CAM_table.txt', 'r') as file:

    for line in file:
        if len(line.split()) == 4:
            if len(line.split()[1].split('.')) == 3:
                print("{:6} {:14} {:6}".format(line.split()[0], line.split()[1], line.split()[3]))
                file_list.append("{:6} {:14} {:6}".format(line.split()[0], line.split()[1], line.split()[3]))


print(file_list)





