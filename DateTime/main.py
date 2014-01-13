'''
Created on 2013/12/16

@author: Robert
'''
import time
t = time.time()
print t
time.sleep(1)
t = time.time()
print t
print "0x%X" % t
print time.strftime('%Y-%m-%d', time.localtime(t))
t = time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(t)), '%Y-%m-%d'))
print t
print "0x%X" % t
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t+86400))
t = time.strptime("2013-12-25", '%Y-%m-%d')
print t
tt = time.mktime(t)
print "tt/86400=%d,0x%x" % (int(tt/86400),int(tt/86400))
print "tt/86400=" , tt/86400
print "tt=%d,0x%x" % (tt,tt)
tt = 0xFFFFFFFF
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tt))