'''
Created on 2014/3/20
@author: Robert
'''
import wx
import wx.lib.newevent
import sys
import os
import threading
import logging
import time
####Thread event
myEVT_ThreadDone = wx.NewEventType()
EVT_ThreadDone = wx.PyEventBinder(myEVT_ThreadDone, 1)
myEVT_ThreadStart = wx.NewEventType()
EVT_ThreadStart = wx.PyEventBinder(myEVT_ThreadStart, 2)
class ThreadingManagement(object):
    thrd           = None
    thrd_stop      = True
    thrd_stop_done = True
    def __init__(self):
        self.Bind(EVT_ThreadDone , self.OnThreadDone)
        self.Bind(EVT_ThreadStart , self.OnThreadStart)
    def ThreadStart( self , target = None, args = ()):
        logging.debug("%s:ThreadStart" % self.__class__.__name__)
        wx.PostEvent(wx.GetTopLevelParent(self), wx.PyCommandEvent(myEVT_ThreadStart, -1))
        self.thrd_stop = False
        self.thrd_stop_done = False
        self.thrd = threading.Thread(target = target,args = args).start()
    def OnThreadStart( self , event ):
        logging.debug("%s:OnThreadStart" % self.__class__.__name__)
        self.thrd_stop = False
        self.thrd_stop_done = False
        if(event):
            event.Skip()
    def ThreadDone( self ):
        logging.debug("%s:ThreadDone" % self.__class__.__name__)
        self.thrd_stop_done = True
        wx.PostEvent(wx.GetTopLevelParent(self), wx.PyCommandEvent(myEVT_ThreadDone, -1))
        logging.info("Done")
    def OnThreadDone( self , event ):
        self.thrd_stop_done = True
        logging.debug("%s:OnThreadDone" % self.__class__.__name__)
        if(event):
            for child in self.GetChildren():
                child.Enable(True)
            #logging.info("Done")
            event.Skip()
    def ThreadStop( self ):
        logging.debug("%s:ThreadStop" % self.__class__.__name__)
        self.thrd_stop = True
        busy = wx.BusyInfo("One moment please, waiting for stopping")
        i = 0
        while(not self.thrd_stop_done):
            time.sleep(0.1)
            i+=1
            if(not i&0xF):
                wx.Yield()
if __name__ == '__main__':
    pass