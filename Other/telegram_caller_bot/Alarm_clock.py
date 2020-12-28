import serial
import time

#ser = serial.Serial('COM4', 115200)
#print("COM Port:")
#print(ser.name);
#print("opened!")
#print("")

def func_ok_nok():
	x="NOK"
	while True:
		x = ser.readline()
		if x == "OK\r\n":
			print (x)
			break
		elif x == "ERROR\r\n":
			print (x)
			break
		else:
			print (x)
			break
def func_dial(command):
	ser.write(command + '\r\n')

def launch_test():
    func_dial('ATH')
    time.sleep(20)
    func_dial('ATD *55*1111#' + ';')
#func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    time.sleep(20)
    func_dial('ATD #55#' + ';')
    #func_ok_nok()
    time.sleep(20)
    func_dial('ATH')
    ser.close()

if __name__ == '__main__':
     launch_test()