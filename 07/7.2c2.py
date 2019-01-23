from sys import argv

src_filename, dst_filename = argv[1:]

ignore = ['duplex', 'alias', 'Current configuration']

with open(src_filename, 'r') as src_file, open(dst_filename, 'w') as dst_file:
    for line in src_file:
        print_line = True
        for word in ignore:
            if word in line.rstrip():
                print_line = False
        if print_line:
            dst_file.write(line)





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



