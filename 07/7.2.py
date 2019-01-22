with open('config_sw1.txt', 'r') as file:
    for line in file:
        if not line.startswith('!'):
            print(line.rstrip())
