list_of_strings = []

with open('CAM_table.txt', 'r') as file:

    for line in file:
        if len(line.split()) == 4:
            if len(line.split()[1].split('.')) == 3:
                #print("{:6} {:16} {:6}".format(line.split()[0], line.split()[1], line.split()[3]))
                list_of_strings.append("{:6} {:16} {:6}".format(line.split()[0], line.split()[1], line.split()[3]))
#print(list_of_strings)

list_of_strings.sort()

#print(list_of_strings)

for line in list_of_strings:
    print(line)






