'''
Created on 2013/12/11

@author: Robert
'''
import random
import sys

checksum = 0
f = open(r'D:\checksum.txt',"w")
for idx in range(int(sys.argv[1])):
    data = random.randint(16,255)
    checksum = checksum + data
    f.write("%02X," % data)

checksum = ((checksum &0xFF)+0x01)&0xFF
f.write("%02X" % checksum)
f.close()