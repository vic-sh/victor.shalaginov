import sys, os
import subprocess
import time
# import admin
from subprocess import Popen, PIPE
from subprocess import check_output

menu_actions = {}


def main_menu():
    print("Please choose the menu you want to start:")
    print("1. Add")
    print("2. Test")
    print("3. Stop")
    print("4. Stats")
    print("5. Clear")
    print("0. Quit")
    choice = input(">>Select>> ")
    exec_menu(choice)
    return


def exec_menu(choice):
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


def add():
    link = input(">> Give link >>")
    console = subprocess.check_output(
        'CD C:/Program Files/Transmission & transmission-remote -a ' + link + ' -w C:/nul', shell=True)
    os.system('cls')
    print(console.decode())
    menu_actions['main_menu']()
    return


def test():
    os.system('cls')
    input_path = 'C:/Users/work/Desktop/torrentin/'
    output_path = 'C:/Users/work/Desktop/torrentout'
    torrents = []
    for r, d, f in os.walk(input_path):
        for file in f:
            if '.torrent' in file:
                torrents.append(os.path.join(r, file))
    console = subprocess.check_output(
        'CD C:/Program Files/Transmission & transmission-remote -t all --remove-and-delete', shell=True)
    for i in torrents:
        st = 'CD C:/Program Files/Transmission & transmission-remote -a ' + i + ' -w ' + output_path + ' -d 1000'
        print(st)
        console = subprocess.check_output(st, shell=True)
        print(console.decode())

    dspeeds = []
    uspeeds = []
    peers = []
    time.sleep(5)
    tout = 3600
    teach = 5
    timeout = time.time() + tout
    tnow = time.time()
    print("Timer start (" + str(tout) + "s)")
    while time.time() < timeout:
        console = subprocess.check_output('CD C:/Program Files/Transmission & transmission-remote -t all -i',
                                          shell=True)
        substr = console.decode().split('NAME')
        st = []
        eta = []
        for s in substr[1:]:
            st.append(s[s.find(':', s.find('State')) + 2:s.find('\n', s.find('State'))])
            eta.append(s[s.find(':', s.find('ETA')) + 2:s.find('\n', s.find('ETA'))])
            ds = float(s[s.find(':', s.find('Download Speed')) + 2:s.find('/s', s.find('Download Speed')) - 3])
            if s[s.find('B/s', s.find('Download Speed')) - 1:s.find('B/s', s.find('Download Speed'))] == 'k':
                dspeeds.append(ds * 1024)
            elif s[s.find('B/s', s.find('Download Speed')) - 1:s.find('B/s', s.find('Download Speed'))] == 'M':
                dspeeds.append(ds * 1024 * 1024)
            us = float(s[s.find(':', s.find('Upload Speed')) + 2:s.find('/s', s.find('Upload Speed')) - 3])
            if s[s.find('B/s', s.find('Upload Speed')) - 1:s.find('B/s', s.find('Upload Speed'))] == 'k':
                uspeeds.append(us * 1024)
            elif s[s.find('B/s', s.find('Upload Speed')) - 1:s.find('B/s', s.find('Upload Speed'))] == 'M':
                uspeeds.append(us * 1024 * 1024)
            peers.append(int(s[s.find(' ', s.find('connected to')) + 4:s.find(',', s.find('connected to'))]))
        if time.time() > tnow + teach:
            os.system('cls')
            print("Time: " + str(int(time.time() - tnow)))
            for i in st:
                print("State: " + i)
            for j in eta:
                print("ETA: " + j)

            if int(max(dspeeds)) > 1024 * 1024:
                print("Max D Speed: " + str(int(max(dspeeds) / (1024 * 1024))) + " MB/s")
            elif int(max(dspeeds)) > 1024:
                print("Max D Speed: " + str(int(max(dspeeds) / 1024)) + " KB/s")
            else:
                print("Max D Speed: " + str(int(max(dspeeds))) + " B/s")

            if int(max(uspeeds)) > 1024 * 1024:
                print("Max U Speed: " + str(int(max(uspeeds) / (1024 * 1024))) + " MB/s")
            elif int(max(uspeeds)) > 1024:
                print("Max U Speed: " + str(int(max(uspeeds) / 1024)) + " KB/s")
            else:
                print("Max U Speed: " + str(int(max(uspeeds))) + " B/s")

            print("Max Peers: " + str(int(max(peers))))

            if int(sum(dspeeds) / len(dspeeds)) > 1024 * 1024:
                print("Avg D Speed: " + str(int(sum(dspeeds) / len(dspeeds) / (1024 * 1024))) + " MB/s")
            elif int(sum(dspeeds) / len(dspeeds)) > 1024:
                print("Avg D Speed: " + str(int(sum(dspeeds) / len(dspeeds) / 1024)) + " KB/s")
            else:
                print("Avg D Speed: " + str(int(sum(dspeeds) / len(dspeeds))) + " B/s")

            if int(sum(uspeeds) / len(uspeeds)) > 1024 * 1024:
                print("Avg U Speed: " + str(int(sum(uspeeds) / len(uspeeds) / (1024 * 1024))) + " MB/s")
            elif int(sum(uspeeds) / len(uspeeds)) > 1024:
                print("Avg U Speed: " + str(int(sum(uspeeds) / len(uspeeds) / 1024)) + " KB/s")
            else:
                print("Avg U Speed: " + str(int(sum(uspeeds) / len(uspeeds))) + " B/s")

            print("Avg Peers: " + str(int(sum(peers) / len(peers))))
            teach = teach + 5

    console = subprocess.check_output('CD C:/Program Files/Transmission & transmission-remote --torrent all --stop',
                                      shell=True)
    menu_actions['main_menu']()
    return


def stop():
    os.system('cls')
    console = subprocess.check_output('CD C:/Program Files/Transmission & transmission-remote --torrent all --stop',
                                      shell=True)
    print(console.decode())
    menu_actions['main_menu']()
    return


def stats():
    os.system('cls')
    console = subprocess.check_output('CD C:/Program Files/Transmission & transmission-remote -t all -i', shell=True)
    print(console.decode())
    substr = console.decode().split('NAME')
    for s in substr[1:]:
        print("Name: " + s[s.find(':', s.find('Name:')) + 2:s.find('\n', s.find('Name:'))])
        print("Download Speed: " + s[s.find(':', s.find('Download Speed')) + 2:s.find('\n', s.find('Download Speed'))])
        print("Upload Speed: " + s[s.find(':', s.find('Upload Speed')) + 2:s.find('\n', s.find('Upload Speed'))])
        print("Percent Done: " + s[s.find(':', s.find('Percent Done')) + 2:s.find('\n', s.find('Percent Done'))])
        print("Peers: " + s[s.find(' ', s.find('connected to')) + 4:s.find(',', s.find('connected to'))])
        print("Seeds: " + s[s.find(' ', s.find('uploading to')) + 4:s.find(',', s.find('uploading to'))])
        print("Leechers: " + s[s.find(' ', s.find('downloading from')) + 6:s.find('\n', s.find('downloading from'))])
        print("\n")
    menu_actions['main_menu']()
    return


def clear():
    os.system('cls')
    console = subprocess.check_output(
        'CD C:/Program Files/Transmission & transmission-remote -t all --remove-and-delete', shell=True)
    print(console.decode())
    menu_actions['main_menu']()
    return


def exit():
    sys.exit()


menu_actions = {
    'main_menu': main_menu,
    '1': add,
    '2': test,
    '3': stop,
    '4': stats,
    '5': clear,
    '0': exit,
}

if __name__ == "__main__":
    # if not admin.isUserAdmin():
    # admin.runAsAdmin()
    # subprocess.run(['sc', 'start', 'Transmission'])
    main_menu()