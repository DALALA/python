'''
Created on 2013/10/11

@author: DALALA
'''
import serial
import time
class AT_Tesrtor():
    def __init__(self,serial_port_number):
        self.serial_com = serial.Serial(serial_port_number)
        self.serial_com.baudrate = 9600
        print (self.serial_com)

    def AT_send(self,AT_Command):
        # add for python 3 version
        print "Send:",AT_Command
        AT_Command = AT_Command + "\r\n" #AT command MUST be ended by: "\r\n"
        AT_Command = bytes(AT_Command)
        self.serial_com.write(AT_Command)
        time.sleep(0.05)
        len = self.serial_com.inWaiting()
        ReceiveStr = self.serial_com.read(len)
        print "Receive:" , ReceiveStr
        return ReceiveStr

if __name__=='__main__':
    ser09 = AT_Tesrtor(3) # this is COM4
    #ser09.AT_send("AT")
    #~ ser09.AT_send("AT+CSQ")
    while(1):
        ser09.AT_send("AT")
        #ser09.AT_send("ATD10086;")
        #time.sleep(10)
        #ser09.AT_send("AT+CHUP")
        time.sleep(2)
        ser09.AT_send("AT+UART?")
        time.sleep(3)
    #~ ser09.AT_send("AT+CIMI")
    #~ ser09.AT_send("AT+CGMR")
