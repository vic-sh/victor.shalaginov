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
			print 'In console = ',x
			break
		elif x == "ERROR\r\n":
			print 'In console = ',x
			break
		else:
			print 'In console = ',x
			break
def func_dial(command):
	ser.write(command + '\r\n')
print("SUBSCRIBE must be enabled!")
print("enabling hotline on number")
print number
func_dial('ATD *53*' + number + '#' + ';')
func_ok_nok()
time.sleep(20)
func_dial('ATH')
time.sleep(10)
print("onhook! check INVITE")
func_dial('ATD !' + ';')
time.sleep(40)
func_dial('ATH')
time.sleep(10)
print("disabling hotline")
func_dial('ATD #53#' + ';')
func_ok_nok()
time.sleep(20)
func_dial('ATH')
ser.close()
