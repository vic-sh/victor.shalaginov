ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as file:
    for line in file:
        print_line = True
        if not line.startswith('!'):
            for word in ignore:
                if word in line.rstrip():
                    print_line = False
            if print_line:
                print(line.rstrip())




            '''while not word_in_ignore:
                for word in ignore:
                    if word in line.rstrip():
                        word_in_ignore = True
                    else:
                        word_in_ignore = False
                    print(line.rstrip())'''



            '''for word in ignore:
                if word in line.rstrip():
                    print("!!!")
                else:
                    print(line.rstrip())
                    '''



