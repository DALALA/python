# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import os
import wx
import win32com.client
import pythoncom
import wx.lib.filebrowsebutton as filebrowse
import wx.lib.agw.pybusyinfo as PBI
# Implementing MainFrame
class MainFrame( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
        bSizer = wx.BoxSizer( wx.VERTICAL )
        self.m_SRCDBB = filebrowse.DirBrowseButton(self, -1, size=(-1, -1), labelText = u"來源資料夾", changeCallback = self.DirBrowseCallBack)
        self.m_DSTDBB = filebrowse.DirBrowseButton(self, -1, size=(-1, -1), labelText = u"目的資料夾")
        bSizer_Sel = wx.BoxSizer( wx.HORIZONTAL )
        self.m_SelectAll    = wx.Button( self, wx.ID_ANY, u"Select"   )
        self.m_DisSelectAll = wx.Button( self, wx.ID_ANY, u"DisSelect")
        self.m_Convert      = wx.Button( self, wx.ID_ANY, u"Convert"  )
        bSizer_Sel.Add( self.m_SelectAll     , 0, wx.ALL | wx.EXPAND, 5 )
        bSizer_Sel.Add( self.m_DisSelectAll  , 0, wx.ALL | wx.EXPAND, 5 )
        bSizer_Sel.Add( self.m_Convert       , 0, wx.ALL | wx.EXPAND, 5 )
        self.m_FileList = wx.CheckListBox( self, style = wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
        bSizer.Add( self.m_SRCDBB  , 0, wx.ALL | wx.EXPAND, 5 )
        bSizer.Add( self.m_DSTDBB  , 0, wx.ALL | wx.EXPAND, 5 )
        bSizer.Add( bSizer_Sel     , 0, wx.ALL | wx.EXPAND, 5 )
        bSizer.Add( self.m_FileList, 1, wx.ALL | wx.EXPAND, 5 )
        self.SetSizer( bSizer )
        self.Layout()
        bSizer.Fit( self )
        self.m_SelectAll.Bind(wx.EVT_BUTTON, self.OnSelectAll)
        self.m_DisSelectAll.Bind(wx.EVT_BUTTON, self.OnDisSelectAll)
        self.m_Convert.Bind(wx.EVT_BUTTON, self.OnConvert)
        self.m_SRCDBB.textControl.SetValue(r'D:\work\RD_Project\RHINO\SPEC\Error Code')
        self.m_DSTDBB.textControl.SetValue(r'D:\work\RD_Project\RHINO\SPEC\Error Code')
        
    def OnConvert(self,event):
        event.Skip()
        pythoncom.CoInitialize()
        wdFormatPDF = 17
        WordApp = win32com.client.DispatchEx('Word.Application')
        WordApp.Visible = 0
        WordApp.DisplayAlerts = 0
        try:
            for f in self.m_FileList.GetCheckedStrings():
                Name,Ext    = os.path.splitext(f)
                nf = "%s\%s.pdf"  % (self.m_SRCDBB.GetValue(),Name)
                f  = "%s\%s.docx" % (self.m_DSTDBB.GetValue(),Name)
                busy = PBI.PyBusyInfo("Starting Convert %s to %s" % (f,nf), parent=self, title="Converting....")
                print f, nf
                WordDoc = WordApp.Documents.Open(f)
                WordDoc.SaveAs(nf,FileFormat=wdFormatPDF)
                WordDoc.Close(SaveChanges=0)
                del busy
        except:
            exc_type, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("%s:line %d: %s" % (fname,exc_tb.tb_lineno,exc_type))
        finally:
            WordApp.Quit()
            del WordApp
    def OnSelectAll(self,event):
        for i in range(self.m_FileList.GetCount()):
            self.m_FileList.Check(i,True)
    def OnDisSelectAll(self,event):
        for i in range(self.m_FileList.GetCount()):
            self.m_FileList.Check(i,False)
    def DirBrowseCallBack(self,event):
        self.m_FileList.Clear()
        if(os.path.isdir(event.GetString())):
            for f in os.listdir(event.GetString()):
                if f.endswith(".docx"):
                    self.m_FileList.Append(f)
if __name__=='__main__':
    app = wx.App()
    my_frame = MainFrame(None)
    #my_frame.Maximize()
    my_frame.Center()
    my_frame.Show()
    app.MainLoop()