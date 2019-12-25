# -*- coding: utf-8 -*-

import serial
import time

number = '2235896'

ser = serial.Serial('COM4', 115200)

def func_ok_nok():
    x = "NOK"
    while True:
        x = ser.readline()
        if x == "OK\r\n":
            print(x)
            break
        elif x == "ERROR\r\n":
            print(x)
            break
        else:
            print(x)
            break

def func_dial(command):

    ser.write((command + '\r\n').encode())

def launch_test(test_number=number):

    func_dial('AT')
    func_ok_nok()
    time.sleep(1)
    func_dial('ATD' + test_number + ';')
    func_ok_nok()
    print("calling"),
    print(test_number)
    print
    time.sleep(20)
    print("sending dtmf")
    array_dtmf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '#']
    for i in array_dtmf:
        print('digit'),
        print(i)
        func_dial('ATD' + i + ';')
        time.sleep(1)
    time.sleep(3)
    func_dial('ATH')
    print('')
    print("The end")
#    ser.close()
#    print("Port closed")
#    print(ser.close())
    time.sleep(5)

def launch_test_alarm():
    func_dial('ATH')
    #func_ok_nok()
    time.sleep(5)
    func_dial('ATD *55*1111#' + ';')
    time.sleep(10)
    print('alarm activated')
    func_dial('ATH')
    time.sleep(5)
    func_dial('ATD #55#' + ';')
    time.sleep(10)
    print('alarm deactivated')
    func_dial('ATH')
    #ser.close()

def launch_test_prohib():
#    ser.write(command + '\r\n')
    number = '89263977957'
    print('Configuring code pass 1111')
    func_dial('ATD *30*1111#' + ';')
    func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    time.sleep(10)
    print('Activating call prohibition C=2')
    func_dial('ATD *34*1111*2#' + ';')
    func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    time.sleep(10)
    print('Trying to dial'),
    print (number)
    print('487 Request terminated expected')
    func_dial('ATD' + number + ';')
    time.sleep(20)
    func_dial('ATH')
    time.sleep(10)
    print('Deactivating call prohibition')
    func_dial('ATD #34*1111#' + ';')
    func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    print('The end')

def launch_test_hotline():
    #ser.write(command + '\r\n')
    number = '89263977957'
    print("SUBSCRIBE must be enabled!")
    print("enabling hotline on number")
    print(number)
    func_dial('ATD *53*' + number + '#' + ';')
    func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    time.sleep(10)
    print('onhook! check INVITE')
    func_dial('ATD' + ';')
    time.sleep(40)
    func_dial('ATD 11111' + ';')
    time.sleep(10)
    func_dial('ATH')
    time.sleep(10)
    print('disabling hotline')
    func_dial('ATD #53#' + ';')
    func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    #ser.close()

if __name__ == '__main__':
    launch_test()

