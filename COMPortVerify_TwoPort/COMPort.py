# -*- coding: utf-8 -*-
'''
Created on 2014/2/23
@author: RobertChen
'''
import serial
import serial.tools.list_ports
import logging
#Global Function
def ToByteArray(value,nByte):
    rlt = list()
    for _ in range(nByte):
        rlt.append(value&0xFF)
        value >>= 8
    rlt.reverse()
    return rlt
def ByteArrayToStr(buf,sp=' '):
    rlt = ''
    for d in buf:
        if d==None:
            rlt += ('XX'+sp)
        else:
            rlt += ('%02X'+sp) % d
    return rlt
def CharArrayToStr(buf,sp=' '):
    rlt = ''
    for d in buf:
        if d==None:
            rlt += ('XX'+sp)
        else:
            rlt += ('%02X'+sp) % ord(d)
    return rlt
def GetCOMPorts():
    return serial.tools.list_ports.comports()
def UpdateCOMPortUsage():
    for port in gCOMUsage.keys():
        gCOMUsage[port] = True #treat as un-available
    for com_port in serial.tools.list_ports.comports():
        try:
            com_serial = serial.Serial(port = com_port[0])
            com_serial.close()
            gCOMUsage[com_port[0]] = False #available
        except:
            gCOMUsage[com_port[0]] = True #treat as un-available
def CRC8(crcpoly,data,init):
    rlt = init
    for d in data:
        rlt ^= d
        for i in range(8):
            if((rlt&0x80)!=0):
                rlt = (rlt<<1)^crcpoly
            else:
                rlt = (rlt<<1)
        #end of for i in range(8):
    #end of for d in data:
    return rlt&0xFF
def ttx(txini,txinc,txopd,txlen):
    ttxd = bytearray(txlen)
    for i in range(txlen):
        if(i==0):
            ttxd[i] = ((txini + txinc) ^ txopd)&0xFF
        else:
            ttxd[i] = ((ttxd[i-1] + txinc) ^ txopd)&0xFF
    return ttxd
#Global Class
class COMPort(serial.Serial):
    ReadBuffer = []
    def __init__(self):
        serial.Serial.__init__(self,baudrate=115200,stopbits=serial.STOPBITS_TWO,timeout=0.05)
    def connect(self,port):
        if(port!=None or port!='None'):
            try:
                #print "self.port=%s,port=%s,self.port==port=%d" % (self.port,port,self.port==port)
                if(self.port!=port):
                    self.ReadBuffer = []
                    if(gCOMUsage[port]):
                        #print "connect error: why %s is used" % port
                        raise
                    else:
                        if(self.port!=None):
                            gCOMUsage[self.port] = False
                        self.port = port
                        gCOMUsage[port] = True
                #end of if(self.port!=port):
                if(not self._isOpen):
                    self.open()
                    #print "open port done"
                return True
            #except:
            except Exception as err:
                #print "connect error : %s,current is %s" % (port , self.portstr)
                #print err
                self.disconnect()
                return False
        #end of if(port!=None):
        return False
    def disconnect(self):
        if(self.port!=None):
            gCOMUsage[self.port] = False
        self.close()
        self.port = None
        self.ReadBuffer = []
    def read(self, size=1):
        rlt = list()
        try:
            read = serial.Serial.read(self,size)
        except Exception as err:
            logging.error("read error:" + err.message)
            read = bytes()
        for d in read:
            rlt.append(ord(d))
        return rlt
    def write(self,data):
        try:
            if(logging.getLogger().isEnabledFor(logging.DEBUG)):
                if(isinstance(data,list)):
                    logging.debug("write:%s" %  ByteArrayToStr(data))
                elif(isinstance(data,str)):
                    logging.debug("write:%s(%s)" %  (CharArrayToStr(data),data))
                else:
                    logging.error("write: unknown type:%s" % type(data))
            nByteWritten = serial.Serial.write(self,data)
            logging.debug("write %d Bytes" % nByteWritten)
            return nByteWritten
        except Exception as err:
            logging.error("write error:" + err.message)
            return 0
    def FlushReadBuffer(self):
        self.ReadBuffer = []
    def readFrame(self,timeout=0.05,MaxSkipBytes=256):
        orgTimeOut = self.timeout
        self.timeout = timeout
        skip_data  = []
        _data    = []
        bFind = False
        while(not bFind):
            if(len(skip_data)<=MaxSkipBytes):
                if(len(self.ReadBuffer)==0):
                    d = self.read()
                else:
                    d = [self.ReadBuffer.pop(0)]
            else:
                #trap to force into the break loop
                d = None
            if(not d):
                if(len(_data)):
                    while(len(_data)>4):
                        LEN=_data[4]
                        if(len(_data)>(LEN+5)):
                            CS = _data[LEN+5]
                            if(CS==GetCheckSum(_data[2:LEN+5])):
                                bFind = True
                                for i in range(LEN+6,len(_data)):
                                    self.ReadBuffer.append(_data.pop(LEN+6))
                                break
                            #end of if(CS==GetCheckSum(_data[2:LEN+5])):
                            else:
                                while(len(_data)):
                                    skip_data.append(_data.pop(0))
                                    if(len(_data)==1 and _data[0]==0xFF):
                                        break
                                    elif(len(_data)>1 and _data[0]==0xFF and _data[1]==0xFF):
                                        break
                                #end of while(len(_data)):
                            #end of else of if(CS==GetCheckSum(_data[2:LEN+5])):
                        #end of if(len(_data)>(LEN+5)):
                        else:
                            while(len(_data)):
                                skip_data.append(_data.pop(0))
                                if(len(_data)==1 and _data[0]==0xFF):
                                    break
                                elif(len(_data)>1 and _data[0]==0xFF and _data[1]==0xFF):
                                    break
                            #end of while(len(_data)):
                        #end of else of if(len(_data)>(LEN+5)):
                    #end of while(len(_data)>4):
                    else:
                        skip_data.extend(_data)
                        _data = []
                    #else of while(len(_data)>4):
                #end of if(len(_data)):
                break
            #end of if(not d):
            else:
                d = d[0]
                if(len(_data)==0):
                    if(d==0xFF):
                        _data.append(d)
                    else:
                        skip_data.append(d)
                #end of if(len(_data)==0):
                elif(len(_data)==1):
                    if(d==0xFF):
                        _data.append(d)
                    else:
                        skip_data.append(_data[0])
                        skip_data.append(d)
                        _data = []
                #end of elif(len(_data)==1):
                else:
                    if(len(_data)==2 and d==0xFF):
                        #avoid 0xFF,0xFF,0xFF case
                        skip_data.append(d)
                    else:
                        _data.append(d)
                #end of else of elif(len(_data)==1):
                while(len(_data)>4):
                    LEN=_data[4]
                    if(len(_data)>(LEN+5)):
                        CS = _data[LEN+5]
                        if(CS==GetCheckSum(_data[2:LEN+5])):
                            bFind = True
                            break
                        #end of if(CS==GetCheckSum(_data[2:LEN+5])):
                        else:
                            while(len(_data)):
                                skip_data.append(_data.pop(0))
                                if(len(_data)==1 and _data[0]==0xFF):
                                    break
                                elif(len(_data)>1 and _data[0]==0xFF and _data[1]==0xFF):
                                    break
                            #end of while(len(_data)):
                        #end of else of if(CS==GetCheckSum(_data[2:LEN+5])):
                    #end of if(len(_data)>(LEN+5)):
                    else:
                        break
                    #end of else of if(len(_data)>(LEN+5)):
                #end of while(len(_data)>4):
            #end of else of if(not d):
        #end of while(not bFind):
        self.timeout = orgTimeOut
        if(logging.getLogger().isEnabledFor(logging.DEBUG)):
            logging.debug( "skip:%s" %  ByteArrayToStr(skip_data))
            logging.debug( "data:%s" %  ByteArrayToStr(_data))
        return skip_data,_data
#Global variable
gCOMSerial = COMPort()
gCOMBT     = COMPort()
gCOMUsage  = dict()
gConnectStatus = list()
if __name__ == '__main__':
    def DummyRead(size=1):
        global TestCOMBuffer
        rlt = list()
        for i in range(size):
            if(len(TestCOMBuffer)==0):
                return rlt
            rlt.append(TestCOMBuffer.pop(0))
        return rlt
    def DummyWrite(data):
        global TestCOMBuffer
        TestCOMBuffer.extend(data)
        return len(data)
    def DummyFlush():
        global TestCOMBuffer
        TestCOMBuffer = []
    def TestReadPorcess(idx,buf,exp):
        if(idx!=None):
            logging.debug('#Test read #%02d' % idx)
        gCOMSerial.write(buf)
        rlt = gCOMSerial.read()
        #if(len(rlt)!=2 or len(exp)!=2):
        #    return False
        if(rlt[0]!=exp[0] or rlt[1]!=exp[1]):
            for i in range(len(rlt)):
                logging.debug('rlt[%d]:%s' % (i ,ByteArrayToStr(rlt[i])))
                logging.debug('exp[%d]:%s' % (i ,ByteArrayToStr(exp[i])))
            return False
        #end of if(rlt[0]!=exp[0] or rlt[1]!=exp[1]):
        return True
    gCOMSerial.read = DummyRead
    gCOMSerial.write = DummyWrite
    gCOMSerial.flush = DummyFlush
    gCOMSerial.flush()
    try:
        logging.debug('#Test read 1B')
        gCOMSerial.write([0xAA,0xBB])
        if(gCOMSerial.read()[0]!=0xAA):
            raise ValueError
        if(gCOMSerial.read()[0]!=0xBB):
            raise ValueError
        logging.debug('#Test read 2B')
        gCOMSerial.write([0xAA,0xBB])
        if(gCOMSerial.read(2)!=[0xAA,0xBB]):
            raise ValueError
        if(not TestReadPorcess(   1,[0xAA,0xBB],[[0xAA,0xBB],[]])):
            raise ValueError
        if(not TestReadPorcess(   2,[0xFF],[[0xFF],[]])):
            raise ValueError
        if(not TestReadPorcess(   3,[0xFF,0xFF],[[0xFF,0xFF],[]])):
            raise ValueError
        if(not TestReadPorcess(   4,[0xFF,0xAA,0xFF],[[0xFF,0xAA,0xFF],[]])):
            raise ValueError
        if(not TestReadPorcess(   5,[0xAA,0xFF,0xFF],[[0xAA,0xFF,0xFF],[]])):
            raise ValueError
        if(not TestReadPorcess(   6,[0xFF,0xFF,0xAA],[[0xFF,0xFF,0xAA],[]])):
            raise ValueError
        if(not TestReadPorcess(   7,[0xAA,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xAA],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(   8,[0xAA,0xFF,0xFF,0x11,0x46,0x00,0xA9,0xBB],[[0xAA],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[0xBB],[]])):
            raise ValueError
        if(not TestReadPorcess(   9,[0xAA,0xFF,0xFF,0x11,0x46,0x00,0xA8],[[0xAA,0xFF,0xFF,0x11,0x46,0x00,0xA8],[]])):
            raise ValueError
        if(not TestReadPorcess(  10,[0xFF,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xFF],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  11,[0xFF,0xFF,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xFF,0xFF],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  12,[0xFF,0xFF,0x11,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xFF,0xFF,0x11],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  13,[0xFF,0xFF,0x11,0x46,0xFF,0xFF,0x11,0x47,0x00,0xA8,0xFF],[[0xFF,0xFF,0x11,0x46],[0xFF,0xFF,0x11,0x47,0x00,0xA8]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[0xFF],[]])):
            raise ValueError
        if(not TestReadPorcess(  14,[0xFF,0xFF,0x11,0x46,0x00,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xFF,0xFF,0x11,0x46,0x00],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  15,[0xFF,0xFF,0x11,0xFF,0xFF,0x11,0x46,0x00,0xA8],[[0xFF,0xFF,0x11,0xFF,0xFF,0x11,0x46,0x00,0xA8],[]])):
            raise ValueError
        if(not TestReadPorcess(  16,[0xFF,0xFF,0x11,0x46,0x00,0xFF,0xFF,0x11,0x46,0x00,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[0xFF,0xFF,0x11,0x46,0x00,0xFF,0xFF,0x11,0x46,0x00],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  17,[0xFF,0xFF,0x11,0x46,0x00,0xA9,0xFF,0xFF,0x11,0x47,0x00,0xA8,0xFF,0xFF,0x11,0x46,0x00,0xA9],[[],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[],[0xFF,0xFF,0x11,0x47,0x00,0xA8]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(  18,[0xAA,0xFF,0xFF,0x11,0x46,0x01,0xCC,0xDC],[[0xAA],[0xFF,0xFF,0x11,0x46,0x01,0xCC,0xDC]])):
            raise ValueError
        if(not TestReadPorcess(  19,[0xAA,0xFF,0xFF,0x11,0x46,0x01,0xCC],[[0xAA,0xFF,0xFF,0x11,0x46,0x01,0xCC],[]])):
            raise ValueError
        if(not TestReadPorcess(  20,[0xAA,0xFF,0xFF,0x11,0x46,0x00,0xA9,0xBB,0xFF,0xFF,0x11,0x47,0x00,0xA8],[[0xAA],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[0xBB],[0xFF,0xFF,0x11,0x47,0x00,0xA8]])):
            raise ValueError
        if(not TestReadPorcess(  21,[0xFF,0xFF,0x11,0x46,0xFF,0xFF,0xFF,0x11,0x46,0x00,0xA9,0xBB,0xFF,0xFF,0x11,0x47,0x00,0xA8],[[0xFF,0xFF,0x11,0x46,0xFF],[0xFF,0xFF,0x11,0x46,0x00,0xA9]])):
            raise ValueError
        if(not TestReadPorcess(None,[],[[0xBB],[0xFF,0xFF,0x11,0x47,0x00,0xA8]])):
            raise ValueError
        logging.info('PASS')
    except ValueError:
        logging.info('FAIL')