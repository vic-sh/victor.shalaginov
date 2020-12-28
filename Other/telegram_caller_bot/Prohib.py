import serial
import time

number = '84957915090'
ser = serial.Serial('/dev/ttyS0', 115200)
print("COM Port:")
print(ser.name);
print("opened!")
print("")

def func_ok_nok():
	x="NOK"
	while True:
		x = ser.readline()
		if x == "OK\r\n":
			print x
			break
		elif x == "ERROR\r\n":
			print x
			break
		else:
			print x
			break
def func_dial(command):
	ser.write(command + '\r\n')
print("Configuring code pass 1111")
func_dial('ATD *30*1111#' + ';')
func_ok_nok()
time.sleep(20)
func_dial('ATH')
time.sleep(10)
print("Activating call prohibition C=2")
func_dial('ATD *34*1111*2#' + ';')
func_ok_nok()
time.sleep(20)
func_dial('ATH')
time.sleep(10)
print("Trying to dial"),
print number
print("487 Request terminated expected")
func_dial('ATD' + number + ';')
time.sleep(40)
func_dial('ATH')
time.sleep(10)
print("Deactivating call prohibition")
func_dial('ATD #34*1111#' + ';')
func_ok_nok()
time.sleep(20)
func_dial('ATH')
print("The end")
ser.close()
