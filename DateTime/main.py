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